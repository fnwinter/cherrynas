from flask_classful import FlaskView, route
from flask import render_template, session

import os

class ExplorerView(FlaskView):
    default_methods = ['GET', 'POST']

    def index(self):
        session['explorer_path'] = '/'

        _path = "/mnt/c/Windows"
        
        folder = [f for f in os.listdir(_path) if os.path.isdir(os.path.join(_path, f))]
        files = [f for f in os.listdir(_path) if os.path.isfile(os.path.join(_path, f))]

        file_list = []
        file_list.append(["..","folder"])
        for f in folder:
            file_list.append([f,"folder"])
        for f in files:
            extension = f[-3:]
            icon = "file"
            if extension == 'txt' or extension == 'log':
                icon = "file-text"
            file_list.append([f,icon])
        
        return render_template('/explorer/explorer.html', files = file_list)

    @route("/test")
    def test(self):
        return "test"