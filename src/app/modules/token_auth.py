import jwt

from app import app

from app.models.User import User

from app.modules import cryption


def token_decode(token) -> tuple:

    try:
        payload = jwt.decode(token, app.secret_key, algorithms=['HS256'])
        user_object = User.query.filter_by(user_email=payload['user_email'], user_pw=payload['user_pw']).first()
        if user_object != None:
            return True, user_object

        return False, 'auth failed'
    except jwt.ExpiredSignatureError:
        return False, 'token expired'
    except jwt.InvalidTokenError:
        return False, 'invalid token'
    except Exception as e:
        return False, "error occured"