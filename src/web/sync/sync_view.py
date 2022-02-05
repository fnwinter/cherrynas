from flask_classful import FlaskView
from flask import render_template, session, redirect

class SyncView(FlaskView):
    """
    Main Page
    """
    default_methods = ['GET', 'POST']

    def index(self):
        """
        main.html
        """
        who = None
        if session.get('nick_name'):
            who = f"{session.get('nick_name')}"
        elif session.get('email'):
            who = f"{session.get('email')}"
        else:
            return redirect('/login')

        return render_template('/main/main.html', email=who)
