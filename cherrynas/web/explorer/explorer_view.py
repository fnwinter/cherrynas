# Copyright 2022 fnwinter@gmail.com

import os
import json

from flask_classful import FlaskView, route
from flask import render_template, session, request, send_file
from utils.file_helper import get_file_size

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(SCRIPT_PATH, os.path.pardir, os.path.pardir, "resources")

class ExplorerView(FlaskView):
    """
    ExplorerView
    - copy, paste, move, delete, upload, download files.
    """
    default_methods = ['GET', 'POST']

    def index(self):
        _path = self.get_current_path()

        folders = [f for f in os.listdir(_path) if os.path.isdir(os.path.join(_path, f))]
        files = [f for f in os.listdir(_path) if os.path.isfile(os.path.join(_path, f))]

        file_list = []
        file_list.append(["..", "folder"])
        for _folder in folders:
            file_list.append([_folder, "folder", "folder"])
        for _file in files:
            _extension = _file[-3:]
            _icon = "file"
            _size = get_file_size(os.path.join(_path, _file))
            if _extension in ['txt', 'log']:
                _icon = "file-text"
            file_list.append([_file, _icon, _size])

        return render_template('/explorer/explorer.html', files=file_list)

    def get_current_path(self):
        _path = None
        if not session.get('current_path'):
            _path = ROOT_PATH
            session['current_path'] = ROOT_PATH
        else:
            _path = session.get('current_path')
        return _path

    @route("/command")
    def command(self):
        command = request.args.get('command')
        option = request.args.get('option')
        result = {"result": "fail"}

        if command == 'double_click':
            _path = session.get('current_path')
            new_path = os.path.join(_path, option)
            if os.path.exists(new_path) and os.path.isdir(new_path):
                session['current_path'] = new_path
                result = {"result" : "refresh"}

        return json.dumps(result)

    @route("/download")
    def download(self):
        args = request.args
        file_name = args.get('file')
        _path = self.get_current_path()
        full_path = os.path.join(_path, file_name)
        # FIXME: check root path
        # FIXME: check login
        return send_file(full_path, as_attachment=True)

    @route("/upload", methods=["POST", "GET"])
    def upload(self):
        return render_template('/explorer/upload.html')

    @route("/uploadFile", methods=["POST", "GET"])
    def uploadFile(self):
        for f in request.files:
            file = request.files[f]
            _path = self.get_current_path()
            file.save(os.path.join(_path, file.filename))
        return ""

    @route("/name", methods=["POST", "GET"])
    def name(self):
        return render_template('/explorer/name.html')