import datetime, random
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    user_pw = db.Column(db.String(500), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    user_job_status = db.Column(db.String(20), nullable=False)
    user_academic_status = db.Column(db.String(20), nullable=False)
    user_specialization = db.Column(db.String(100), nullable=False)
    user_pre_startup = db.Column(db.Boolean, nullable=False)
    user_email_verified = db.Column(db.Boolean, nullable=False)
    user_verify_code = db.Column(db.String(7), nullable=False)
    
    def __init__(self,user_email, user_pw, user_job_status, user_academic_status, user_specialization, user_pre_startup) -> None:
        self.user_email = user_email
        self.user_pw = user_pw
        self.created = datetime.datetime.now()
        self.user_job_status =user_job_status
        self.user_academic_status = user_academic_status
        self.user_specialization = user_specialization
        self.user_pre_startup = user_pre_startup
        self.user_email_verified = False
        self.user_verify_code = ""
        for _ in range(0, 7):
            self.user_verify_code += str(random.randint(0,9))
       
    def __repr__(self) -> str:
        return '<User %r>' % self.email