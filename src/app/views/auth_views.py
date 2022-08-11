from flask import jsonify, Blueprint, request

import jwt, datetime
bp = Blueprint('auth', __name__, url_prefix='/auth')

admin_email = 'admin@admin.kr'
admin_pw = 'admin'
SECRET_KEY = 'secret'

@bp.route("/login", methods=['POST'])
def login_proc():
    if request.is_json:
        params = request.get_json()
        user_email = params['user_email']
        user_pw = params['user_pw']

        # 아이디, 비밀번호가 일치하는 경우
        if (user_email == admin_email and
                user_pw == admin_pw):
            payload = {
                'user_email': user_email,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)  # 로그인 30일 유지
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

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
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return jsonify({'result': 'success', 'user_email': payload['user_email']})
        except jwt.ExpiredSignatureError:
            return jsonify({'result': 'fail', 'message': 'token expired'})
        except jwt.InvalidTokenError:
            return jsonify({'result': 'fail', 'message': 'invalid token'})
        except Exception as e:
            return jsonify({'result': 'fail', 'message': str(e)})
    else:
        return jsonify({'result': 'fail'})