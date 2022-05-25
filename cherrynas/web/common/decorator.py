# Copyright 2022 fnwinter@gmail.com

from functools import wraps
from flask import redirect, session

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not session.get('email'):
            return redirect('/cherry/login')
        return func(*args, **kwargs)
    return decorated_view
