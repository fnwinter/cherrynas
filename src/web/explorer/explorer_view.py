from flask_classful import FlaskView, route
from flask import render_template, session, request

from web.util.file_helper import get_file_size

import os
import json

ROOT_PATH = "/mnt/c/Windows"

class ExplorerView(FlaskView):
    default_methods = ['GET', 'POST']

    def index(self):
        _path = None
        if not session.get('current_path'):
            print("no current_path")
            _path = ROOT_PATH
            session['current_path'] = ROOT_PATH
        else:
            _path = session.get('current_path')

        folders = [f for f in os.listdir(_path) if os.path.isdir(os.path.join(_path, f))]
        files = [f for f in os.listdir(_path) if os.path.isfile(os.path.join(_path, f))]

        file_list = []
        file_list.append(["..","folder"])
        for _folder in folders:
            file_list.append([_folder,"folder","folder"])
        for _file in files:
            _extension = _file[-3:]
            _icon = "file"
            _size = get_file_size(os.path.join(_path,_file))
            if _extension == 'txt' or _extension == 'log':
                _icon = "file-text"
            file_list.append([_file,_icon,_size])
        
        return render_template('/explorer/explorer.html', files = file_list)

    @route("/command")
    def command(self):
        command = request.args.get('command')
        option = request.args.get('option')
        result = { "result": "fail" }

        if command == 'double_click':
            _path = session.get('current_path')
            new_path = os.path.join(_path, option)
            if os.path.exists(new_path) and os.path.isdir(new_path):
                session['current_path'] = new_path
                result = { "result" : "refresh" }

        return json.dumps(result)