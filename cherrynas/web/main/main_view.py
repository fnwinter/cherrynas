import json

from config import SYSTEM_INFO_PATH
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

        system_info_ = None
        with open(SYSTEM_INFO_PATH, 'r') as f:
            system_info_ = json.loads(f.read())

        hardware_ = system_info_.get('hw')
        software_ = system_info_.get('sw')
        disk_ = system_info_.get('disk')
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
