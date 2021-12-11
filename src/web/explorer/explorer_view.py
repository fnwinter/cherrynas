from flask_classful import FlaskView
from flask import render_template, session

import os

class ExplorerView(FlaskView):
    default_methods = ['GET', 'POST']

    def index(self):
        session['explorer_path'] = '/'

        file_list = os.listdir("./")
        return render_template('/explorer/explorer.html', files = file_list)