# Copyright 2022 fnwinter@gmail.com

from flask import redirect, session
from functools import wraps

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not session.get('email'):
            return redirect('/cherry/login')
        return func(*args, **kwargs)
    return decorated_view
