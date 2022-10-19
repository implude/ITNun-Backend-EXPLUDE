# import modules
from flask import jsonify, Blueprint, request

from app.models.User import User
from app.modules import cryption, send_email
from app.modules.form_checker import Auth_checker
from app import db
from app import app

import jwt, datetime

bp = Blueprint('auth', __name__, url_prefix='/auth') # create blueprint


@bp.route("/login", methods=['POST']) # login route
def login_proc():
    if request.is_json: # check if request is json
        params = request.get_json() # get json data
        user_email = params['user_email'] # get user email
        user_pw = cryption.sha256_string(params['user_pw']) # get hashed user password
        user_object = User.query.filter_by(user_email=user_email, user_pw=user_pw).first()
        # if matched user exists
        if user_object: # check if user exists
            if not user_object.user_email_verified:
                return jsonify({"status": "fail", "message": "need email verification"})
            payload = {
                'user_email': user_email,
                'user_pw': user_pw,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)  # token expires in 30 days
            }
            token = jwt.encode(payload, app.secret_key, algorithm='HS256') # encode token

            return jsonify({'result': 'success', 'token': token}) # return token


        # if not not match
        else:
            return jsonify({'result': 'fail'}) # return fail message             
@bp.route("/myinfo", methods=['POST']) # myinfo route
def myinfo_proc():
    if request.is_json:
        params = request.get_json()
        token = params['token']

        try:
            payload = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            return jsonify({'result': 'success', 'user_email': payload['user_email']})
        except jwt.ExpiredSignatureError:
            return jsonify({'result': 'fail', 'message': 'token expired'})
        except jwt.InvalidTokenError:
            return jsonify({'result': 'fail', 'message': 'invalid token'})
        except Exception as e:
            return jsonify({'result': 'fail', 'message': str(e)})
    else:
        return jsonify({'result': 'fail'})


@bp.route("/signup", methods=['POST']) # signup route
def signup_proc():
    if request.is_json: # check if request is json
        params = request.get_json() # get json data
        user_email = params['user_email'] # get user email
        user_pw = cryption.sha256_string(params['user_pw']) # get hashed user password
        user_job_status = params['user_job_status'] # get user job status
        user_academic_status = params['user_academic_status'] # get user academic status
        user_specialization = params['user_specialization'] # get user specialization
        user_pre_startup = params['user_pre_startup'] # get user pre startup
        if not Auth_checker.signup_check(email=user_email, pw=params['user_pw'], job_status=user_job_status, 
                                        academic_status=user_academic_status, specialization=user_specialization, pre_startup=user_pre_startup): # check if signup data is valid
            return jsonify({'result': 'fail', 'message': 'invalid params'}) # return fail by invalid parmeter message
        if User.query.filter_by(user_email=user_email).first(): # check if user exists
            return jsonify({'result': 'fail', 'message': 'user already exists'}) # return fail by user already exists message

        else:
            user = User(
                        user_email=user_email, 
                        user_pw=user_pw,
                        user_job_status=user_job_status,
                        user_academic_status=user_academic_status,
                        user_specialization=user_specialization,
                        user_pre_startup=user_pre_startup) # create user object

            db.session.add(user) # add user to db
            db.session.commit() # commit db
            user = User.query.filter_by(user_email=user_email).first()
            send_email.send_verification_email(user.user_email, user.user_verify_code)
            return jsonify({'result': 'success'}) # return success message

@bp.route("/email_verification", methods=['GET']) # email verification route
def email_verification_get_proc():
    if request.is_json:
        params = request.get_json()
        user_email = params['user_email']
        user_verify_code = params['user_verify_code']
        user_object = User.query.filter_by(user_email=user_email).first()
        if user_object:
            if user_object.user_verify_code == user_verify_code:
                user_object.user_email_verified = True
                db.session.commit()
                return jsonify({'result': 'success'})
            else:
                return jsonify({'result': 'fail', 'message': 'invalid code'})
        else:
            return jsonify({'result': 'fail', 'message': 'user not found'})