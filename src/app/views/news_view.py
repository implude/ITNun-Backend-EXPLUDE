#import modules
from flask import jsonify, Blueprint
import datetime

from app.models.News import News, User_Inquierd_News, Server_Inquired_News
from app.modules import news_crawl
from app import db


bp = Blueprint('news', __name__, url_prefix='/news')


@bp.route('/check_news', methods=['POST'])
def check_news():
    if Server_Inquired_News.query.filter_by(date=datetime.datetime.now).first() == None:
        queue = Server_Inquired_News(date=datetime.datetime.now())
        db.session.add(queue)
        db.session.commit()
        crawled_news = news_crawl.crawl_news()
        #delete all news
        News.query.delete()
        news_object = []
        for data in crawled_news:
            news_object.append(
                News(
                    news_id=data['id'],
                    news_title=data['title'],
                    news_date=data['date'],
                    news_contents=data['content'],
                    news_url=data['url']
                ))
        db.session.add_all(news_object)
        db.session.commit()
        return jsonify({'result': 'success'})
    
        

    
