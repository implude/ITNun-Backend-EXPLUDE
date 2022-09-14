from flask import jsonify, Blueprint,request

from app.models.Policy import Policy, Server_Inquired_Policy, User_Inquierd_Policy
from app.modules import open_api, token_auth

from app import db
import os, datetime

bp = Blueprint('policy', __name__, url_prefix='/policy')


@bp.route('/update_policy', methods=['POST'])
def update_policy():
    if request.is_json:
        try:
            params = request.get_json()
            request_key = params['requset_key']
        except:
            return jsonify({'result': 'fail', 'message': 'invalid params'})
        if request_key == os.environ['REQUEST_KEY']:
            policy_data = open_api.get_youth_policy()
            Policy.query.delete()
            object_list = []
            for i in policy_data:
                object_list.append(Policy(policy_id=i['bizId'], 
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
                                policy_website_url=i['rqutUrla']))
                db.session.add(object_list[-1])
            db.session.commit()
                
            return jsonify({'result': 'success'})
        return jsonify({'result': 'fail', 'message': 'invalid request key'})

@bp.route('/get_policy', methods=['POST'])
def get_policy():
    if request.is_json:
        params = request.get_json()
        try:
            token = params['token']
            print(token)
        except:
            return jsonify({'result': 'fail', 'message': 'token not found'})
        token_auth_info = token_auth.token_decode(token)
        if token_auth_info[0]:
            if Server_Inquired_Policy.query.filter_by(date=datetime.datetime.now().date()).first() == None:
                queue = Server_Inquired_Policy(date=datetime.datetime.now().date())
                db.session.add(queue)
                db.session.commit()
                policy_data = open_api.get_youth_policy()
                Policy.query.delete()
                policy_object = []
                for i in policy_data:
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
                                    policy_website_url=i['rqutUrla']))
                    db.session.add(policy_object[-1])
                db.session.commit()
            else:
                policy_object = Policy.query.all()
            read_policy = User_Inquierd_Policy.query.filter_by(user_id=token_auth_info[1].id).all()

            read_policy_id_list = []
            for ii in read_policy:
                read_policy_id_list.append(ii.policy_id)

            not_read_policy_list = []
            not_read_policy_objetct = []
            for i in policy_object:
                if i.policy_id not in read_policy_id_list:
                    not_read_policy_list.append(i.as_dict())
                    not_read_policy_objetct.append(User_Inquierd_Policy(user_id=token_auth_info[1].id, news_id=i.policy_id))
            db.session.add_all(not_read_policy_objetct)
            db.session.commit()
            return jsonify({"policy": not_read_policy_list})
        else:
            return jsonify({'result': 'fail', 'message': token_auth_info[1]})
    else:
        return jsonify({"result": "invalid request"})