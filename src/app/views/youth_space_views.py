from flask import jsonify, Blueprint,request

from app.modules import open_api, token_auth

from app import db
import os, datetime

bp = Blueprint('youth_space', __name__, url_prefix='/youth_space')

@bp.route('/get_all_youth_space', methods=['POST'])
def get_all_youth_space():
    if request.is_json:
        # params = request.get_json()
        # try:
        #     token = params['token']
        # except:
        #     return jsonify({'result': 'fail', 'message': 'token not found'})
        # token_auth_info = token_auth.token_decode(token)
        # if token_auth_info[0]:
        open_api.get_youth_space()
        return jsonify({'result': 'success'})
        #     return jsonify({"policy": policy_dict_list})
        # else:
        #     return jsonify({'result': 'fail', 'message': token_auth_info[1]})
    else:
        return jsonify({"result": "invalid request"})