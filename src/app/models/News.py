from app import db

import datetime


class News(db.Model):

    news_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    news_title = db.Column(db.String(100), nullable=False)
    news_date = db.Column(db.String(100), nullable=False)
    news_contents = db.Column(db.String(10000), nullable=False)
    news_url = db.Column(db.String(300), nullable=False)

    def __init__(self, news_id, news_title, news_date, news_contents, news_url):
        self.news_id = news_id
        self.news_title = news_title
        self.news_date = datetime.datetime.strptime(news_date, '%Y.%m.%d')
        self.news_contents = news_contents
        self.news_url = news_url

    def __repr__(self) -> str:
        return '<User %r>' % self.email
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class User_Inquierd_News(db.Model):
    
    news_id = db.Column(db.Integer, db.ForeignKey('news.news_id'), nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self) -> str:
        return '<User %r>' % self.email
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Server_Inquired_News(db.Model):
    
    date = db.Column(db.DateTime, nullable=False, primary_key=True)

