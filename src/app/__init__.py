from dotenv import load_dotenv   
import os, secrets
load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
    app.secret_key = secrets.token_bytes(16)
    db = SQLAlchemy(app)

    db.init_app(app)
    db.app = app

    return app, db

app, db = create_app()

from app.models.User import User

db.create_all()

from app.views import main_views, auth_views
app.register_blueprint(main_views.bp)
app.register_blueprint(auth_views.bp)

    
if __name__ == '__main__':
    app.run()