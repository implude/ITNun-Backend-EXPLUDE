from app import db


class Policy(db.Model):

    policy_id = db.Column(db.String(14), unique=True, nullable=False, primary_key=True)
    policy_name = db.Column(db.String(200), nullable=False)
    policy_Biz_code = db.Column(db.String(12), nullable=False)
    policy_type = db.Column(db.String(20), nullable=False)
    policy_description = db.Column(db.String(1500), nullable=False)
    policy_spor_amount = db.Column(db.String(500), nullable=False)
    policy_spor_description = db.Column(db.String(1500), nullable=False)
    policy_age = db.Column(db.String(500), nullable=False)
    policy_job_status = db.Column(db.String(500), nullable=False)
    policy_academic_status = db.Column(db.String(500), nullable=False)
    policy_specialization = db.Column(db.String(500), nullable=False)
    policy_good_at = db.Column(db.String(500), nullable=False)

    def __repr__(self) -> str:
        return '<User %r>' % self.email