from flask import jsonify, Blueprint, request

from app.models.User import User
from app.modules import cryption
from app.modules.form_checker import Auth_checker
from app import db
from app import app

import jwt, datetime
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route("/login", methods=['POST'])
def login_proc():
    if request.is_json:
        params = request.get_json()
        user_email = params['user_email']
        user_pw = cryption.sha256_string(params['user_pw'])

        # 아이디, 비밀번호가 일치하는 경우
        if User.query.filter_by(user_email=user_email, user_pw=user_pw).first() and User.query.filter_by().first():
            payload = {
                'user_email': user_email,
                'user_pw': user_pw,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)  # 로그인 30일 유지
            }
            token = jwt.encode(payload, app.app.secret_key, algorithm='HS256')

            return jsonify({'result': 'success', 'token': token})


        # 아이디, 비밀번호가 일치하지 않는 경우
        else:
            return jsonify({'result': 'fail'})

@bp.route("/myinfo", methods=['POST'])
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


@bp.route("/signup", methods=['POST'])
def signup_proc():
    if request.is_json:
        params = request.get_json()
        user_email = params['user_email']
        user_pw = cryption.sha256_string(params['user_pw'])
        user_birth = params['user_birth']
        user_job_status = params['user_job_status']
        user_academic_status = params['user_academic_status']
        user_specialization = params['user_specialization']
        user_pre_startup = params['user_pre_startup']
        if not Auth_checker.signup_check(user_email, user_pw, user_birth, user_job_status, user_academic_status, user_specialization, user_pre_startup):
            return jsonify({'result': 'fail', 'message': 'invalid params'})
        # 아이디가 이미 존재하는 경우
        if User.query.filter_by(user_email=user_email).first():
            return jsonify({'result': 'fail', 'message': 'user already exists'})

        # 아이디가 존재하지 않는 경우
        else:
            user = User(
                        user_email=user_email, 
                        user_pw=user_pw,
                        user_birth=user_birth,
                        user_job_status=user_job_status,
                        user_academic_status=user_academic_status,
                        user_specialization=user_specialization,
                        user_pre_startup=user_pre_startup)

            db.session.add(user)
            db.session.commit()

            return jsonify({'result': 'success'})