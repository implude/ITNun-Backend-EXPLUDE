from dotenv import load_dotenv   
import os
load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
    db = SQLAlchemy(app)

    from app.views import main_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    db.init_app(app)
    db.app = app

    return app, db

app, db = create_app()

from app.models.User import User

db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    
if __name__ == '__main__':
    app.run()