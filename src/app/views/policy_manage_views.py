from flask import jsonify, Blueprint,request

from app.models.Policy import Policy
from app.modules import open_api

from app import db
import os

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