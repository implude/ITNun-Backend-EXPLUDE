from app import db


class News(db.Model):

    news_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    news_title = db.Column(db.String(100), nullable=False)
    news_date = db.Column(db.String(100), nullable=False)
    news_contents = db.Column(db.String(5000), nullable=False)
    news_url = db.Column(db.String(300), nullable=False)

    def __repr__(self) -> str:
        return '<User %r>' % self.email

class User_Inquierd_News(db.Model):
    
    inquerd_news_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.news_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self) -> str:
         return '<User %r>' % self.email
class Server_Inquired_News(db.Model):
    
    date = db.Column(db.DateTime, nullable=False, primary_key=True)

