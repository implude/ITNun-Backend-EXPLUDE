from app import db


class User(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email