from web import DB

class Account(DB.Model):
    __tablename__ = 'account'
    email = DB.Column(DB.String, primary_key=True, nullable=False)
    nick_name = DB.Column(DB.String(30))
    password = DB.Column(DB.String, nullable=False)
    reset_pin = DB.Column(DB.String(6))
    allowed_by_admin = DB.Column(DB.Boolean, default=False)
