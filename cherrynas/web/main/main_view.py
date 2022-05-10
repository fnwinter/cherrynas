import json
import re

from config import SYSTEM_INFO_PATH
from web.common.helper import get_id
from flask_classful import FlaskView
from flask import render_template, redirect

class MainView(FlaskView):
    """
    Main Page
    """
    default_methods = ['GET', 'POST']

    def index(self):

        who = get_id()
        if not who:
            return redirect('/cherry/login')

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