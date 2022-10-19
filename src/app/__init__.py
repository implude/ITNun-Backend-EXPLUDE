from dotenv import load_dotenv   
import os, secrets
load_dotenv() #load .env file

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(): # create and configure the app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
    app.secret_key = secrets.token_bytes(16)
    db = SQLAlchemy(app)

    db.init_app(app)
    db.app = app

    return app, db

app, db = create_app()

from app.models.User import User
from app.models.Policy import Policy
from app.models.News import News, Server_Inquired_News
db.create_all() # create tables

from app.views import main_views, auth_views, policy_manage_views, news_view, youth_space_views # import views
# register blueprints
app.register_blueprint(main_views.bp)
app.register_blueprint(auth_views.bp)
app.register_blueprint(policy_manage_views.bp)
app.register_blueprint(news_view.bp)
app.register_blueprint(youth_space_views.bp)


    
if __name__ == '__main__':
    app.run() # run the app