from flask_classful import FlaskView
from flask import render_template, session, redirect

class AdminView(FlaskView):
    """
    Admin Page
    """
    default_methods = ['GET', 'POST']

    def index(self):
        """
        admin.html
        """
        is_admin = session.get('admin')
        if is_admin != 'yes':
            redirect('/')

        who = None
        if session.get('nick_name'):
            who = f"{session.get('nick_name')}"
        elif session.get('email'):
            who = f"{session.get('email')}"

        return render_template('/admin/admin.html', email=who)
