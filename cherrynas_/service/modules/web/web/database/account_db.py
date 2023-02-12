# Copyright 2022 fnwinter@gmail.com

from web import DB

class Account(DB.Model):
    """
    Basic account database scheme
    - email : same as ID, unique key
    - joined : when admin allow to join
    - permission : keyword which can define allowed page
    - reset_pin : when member forget the password, send reset pin to email
    """
    __tablename__ = 'account'
    email = DB.Column(DB.String, primary_key=True, nullable=False)
    nick_name = DB.Column(DB.String(30))
    password = DB.Column(DB.String, nullable=False)
    reset_pin = DB.Column(DB.String(6))
    joined = DB.Column(DB.Boolean, default=False)
    permission = DB.Column(DB.String, default='all')
