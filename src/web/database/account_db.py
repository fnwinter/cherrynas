from web import db

class Account(db.Model):
    __tablename__ = 'account'
    email = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    reset_pin = db.Column(db.String(6))
