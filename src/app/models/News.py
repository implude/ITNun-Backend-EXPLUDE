from app import db

import datetime

class News(db.Model):

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, auto_increamnet=True)
    news_title = db.Column(db.String(100), nullable=False)
    news_date = db.Column(db.String(100), nullable=False)
    news_contents = db.Column(db.String(1000), nullable=False)
    news_url = db.Column(db.String(300), nullable=False)

    def __init__(self, news_title, news_date, news_contents, news_url):

        self.news_title = news_title
        self.news_date = datetime.datetime.strptime(news_date, '%Y.%m.%d')
        self.news_contents = news_contents
        self.news_url = news_url

    def __repr__(self) -> str:
        return '<User %r>' % self.email
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Server_Inquired_News(db.Model):
    
    date = db.Column(db.DateTime, nullable=False, primary_key=True)

