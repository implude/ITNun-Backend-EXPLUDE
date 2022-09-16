# import modules
from flask import jsonify, Blueprint,request

from app.models.Policy import Policy, Server_Inquired_Policy, User_Inquierd_Policy
from app.modules import open_api, token_auth

from app import db
import datetime

bp = Blueprint('policy', __name__, url_prefix='/policy') # create blueprint

@bp.route('/get_policy', methods=['POST']) # check get_policy route
def get_policy():
    if request.is_json: # check request is json
        params = request.get_json() # get json data
        try:
            token = params['token'] # get token
        except:
            return jsonify({'result': 'fail', 'message': 'token not found'}) # return fail by token not found message
        token_auth_info = token_auth.token_decode(token) # decode token
        if token_auth_info[0]: # check token is valid
            if Server_Inquired_Policy.query.filter_by(date=datetime.datetime.now().date()).first() == None: # check server inquired policy today
                queue = Server_Inquired_Policy(date=datetime.datetime.now().date()) # add date to server inquired policy
                db.session.add(queue) # add queue to db
                db.session.commit() # commit db
                policy_data = open_api.get_youth_policy() # get youth policy data
                Policy.query.delete() # clear policy table
                policy_object = []
                for i in policy_data: # add policy data to policy object
                    policy_object.append(Policy(policy_id=i['bizId'], 
                                    policy_name=i['polyBizSjnm'], 
                                    policy_Biz_code=i['polyBizSecd'],
                                    policy_type=i['plcyTpNm'], 
                                    policy_description=i['polyItcnCn'], 
                                    policy_spor_amount=i['sporScvl'], 
                                    policy_spor_description=i['sporCn'], 
                                    policy_age=i['ageInfo'], 
                                    policy_job_status=i['empmSttsCn'], 
                                    policy_academic_status=i['accrRqisCn'], 
                                    policy_specialization=i['majrRqisCn'],
                                    policy_good_at=i['splzRlmRqisCn'],
                                    policy_request_deadline=i['rqutPrdCn'],
                                    policy_website_url=i['rqutUrla'],
                                    policy_progress=i['rqutProcCn']
                                    )
                                    )
                    db.session.add(policy_object[-1]) # add policy object to db
                db.session.commit() # commit db
            else: # if server checked policy today
                policy_object = Policy.query.all() # get all policy data
            read_policy = User_Inquierd_Policy.query.filter_by(user_id=token_auth_info[1].id).all() # get user inquired policy

            read_policy_id_list = []
            for ii in read_policy:
                read_policy_id_list.append(ii.policy_id) # make user read policy list

            not_read_policy_list = []
            not_read_policy_objetct = []
            for i in policy_object:
                if i.policy_id not in read_policy_id_list:
                    not_read_policy_list.append(i.as_dict())
                    not_read_policy_objetct.append(User_Inquierd_Policy(user_id=token_auth_info[1].id, policy_id=i.policy_id))
            db.session.add_all(not_read_policy_objetct)
            db.session.commit()
            return jsonify({"policy": not_read_policy_list})
        else:
            return jsonify({'result': 'fail', 'message': token_auth_info[1]})
    else:
        return jsonify({"result": "invalid request"})

@bp.route('/get_all_policy', methods=['POST'])
def get_all_policy():
    if request.is_json:
        params = request.get_json()
        try:
            token = params['token']
        except:
            return jsonify({'result': 'fail', 'message': 'token not found'})
        token_auth_info = token_auth.token_decode(token)
        if token_auth_info[0]:
            policy_dict_list = []
            policy_object = Policy.query.all()
            for i in policy_object:
                policy_dict_list.append(i.as_dict())
            return jsonify({"policy": policy_dict_list})
        else:
            return jsonify({'result': 'fail', 'message': token_auth_info[1]})
    else:
        return jsonify({"result": "invalid request"})
