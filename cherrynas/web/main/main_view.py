from flask_classful import FlaskView
from flask import render_template, session, redirect

class MainView(FlaskView):
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

        hardware_ = { 'cpu' : 'i7-1234', 'ram': '16', 'network':'1234' }
        software_ = { 'cherrynas':'1.0.0', 'os': 'windows' }
        disk_ = {'info':'1TB'}
        alarm_ = None
        login_user_ = 'fnwinter@gmail.com , total 1 person'
        logs_ = ['ftp open \r\n','started','  test']

        return render_template('/main/main.html', 
            email=who,
            hardware=hardware_,
            software=software_,
            disk=disk_,
            alarm=alarm_,
            login_user=login_user_,
            logs=logs_)
