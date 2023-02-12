# Copyright 2022 fnwinter@gmail.com

from flask_classful import FlaskView
from flask import render_template

from web.common.decorator import login_required
from web.common.helper import get_id

class SyncView(FlaskView):
    """
    Sync Page
    """
    default_methods = ['GET', 'POST']

    @login_required
    def index(self):
        """
        sync.html
        """
        who = get_id()

        return render_template('/sync/sync.html', email=who)
