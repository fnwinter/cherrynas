# Copyright 2022 fnwinter@gmail.com

import json

from flask_classful import FlaskView
from flask import render_template

from config import SYSTEM_INFO_PATH
from web.common.decorator import login_required
from web.common.helper import get_id

class MainView(FlaskView):
    """
    Main Page
    """
    default_methods = ['GET', 'POST']

    @login_required
    def index(self):

        who = get_id()
        system_info_ = None
        with open(SYSTEM_INFO_PATH, 'r', encoding="utf8") as f:
            system_info_ = json.loads(f.read())

        hardware_ = system_info_.get('hw')
        software_ = system_info_.get('sw')
        disk_ = system_info_.get('disk')
        alarm_ = None
        login_user_ = f'{who} , total 1 person'
        logs_ = ['ftp open \r\n','started','  test']

        return render_template('/main/main.html',
            email=who,
            hardware=hardware_,
            software=software_,
            disk=disk_,
            alarm=alarm_,
            login_user=login_user_,
            logs=logs_)
