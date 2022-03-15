from web import DB

class Account(DB.Model):
    __tablename__ = 'account'
    email = DB.Column(DB.String, primary_key=True, nullable=False)
    nick_name = DB.Column(DB.String(30))
    password = DB.Column(DB.String, nullable=False)
    reset_pin = DB.Column(DB.String(6))
    joined = DB.Column(DB.Boolean, default=False)
    permission = DB.Column(DB.String, default='all')
