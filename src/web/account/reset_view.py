from flask_classful import FlaskView
from flask import render_template, session

class ResetView(FlaskView):
    def index(self):
        return render_template('/account/reset.html')