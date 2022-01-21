from flask_classful import FlaskView
from flask import render_template, session

class LogoutView(FlaskView):
    def index(self):
        session.pop('email', None)
        session.pop('nick_name', None)
        return render_template('/account/logout.html')
