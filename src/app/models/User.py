from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    user_pw = db.Column(db.String(500), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    user_age = db.Column(db.Integer, nullable=False)
    user_job_status = db.Column(db.String(20), nullable=False)
    user_academic_status = db.Column(db.String(20), nullable=False)
    user_specialization = db.Column(db.String(100), nullable=False)
    user_pre_startup = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email