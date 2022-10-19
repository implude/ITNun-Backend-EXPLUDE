#import modules
from flask import jsonify, Blueprint, request
import datetime

from app.models.News import News, User_Inquierd_News, Server_Inquired_News
from app.modules import news_crawl, token_auth
from app import db


bp = Blueprint('news', __name__, url_prefix='/news')


@bp.route('/check_news', methods=['POST'])
def check_news():
    if request.is_json:
        params = request.get_json()
        try:
            token = params['token']
            print(token)
        except:
            return jsonify({'result': 'fail', 'message': 'token not found'})
        token_auth_info = token_auth.token_decode(token)
        if token_auth_info[0]:
            if Server_Inquired_News.query.filter_by(date=datetime.datetime.now().date()).first() == None:
                queue = Server_Inquired_News(date=datetime.datetime.now().date())
                db.session.add(queue)
                db.session.commit()
                crawled_news = news_crawl.crawl_news()
                news_object = []
                for data in crawled_news:
                    news_object.append(
                        News(
                            news_title=data['title'],
                            news_date=data['date'],
                            news_contents=data['content'],
                            news_url=data['url']
                        ))
                db.session.add_all(news_object)
                db.session.commit()
            else:
                news_object = News.query.all()
            result = []
            for i in news_object:
                    result.append(i.as_dict())
            return jsonify({"news": result})
        else:
            return jsonify({'result': 'fail', 'message': token_auth_info[1]})
    else:
        return jsonify({"result": "invalid request"})
    
        

    
