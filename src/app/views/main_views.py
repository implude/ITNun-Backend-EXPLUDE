#import modules
from flask import jsonify, Blueprint

bp = Blueprint('main', __name__, url_prefix='/') # create blueprint

@bp.route('/check_server', methods=['GET']) # check server route
def check_server():
    return jsonify({'status': 'OK'})
