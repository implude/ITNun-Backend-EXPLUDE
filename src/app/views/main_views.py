#import modules
from flask import jsonify, Blueprint


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/check_server', methods=['GET'])
def check_server():
    return jsonify({'status': 'OK'})
