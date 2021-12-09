from flask_classful import FlaskView
from flask import render_template, session

class MainView(FlaskView):
    default_methods = ['GET', 'POST']

    def index(self):
        email_ = None
        if session.get('email'):
            email_ = f"{session.get('email')}"
        return render_template('/main/main.html', email=email_)