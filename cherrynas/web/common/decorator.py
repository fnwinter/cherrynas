from flask import redirect, session
from functools import wraps

def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if session.get('email'):
            return redirect('/')
        return func(*args, **kwargs)
    return decorated_view
