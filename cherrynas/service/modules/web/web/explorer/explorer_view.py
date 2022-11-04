# Copyright 2022 fnwinter@gmail.com

import os
import json
import shutil

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
    result = {"result": "fail"}

    def __init__(self):
        self.commands = {
            "new_folder": self.new_folder,
            "rename_item": self.rename_item,
            "delete_item": self.delete_item,
            "copy_item": self.copy_item,
            "paste_item": self.paste_item
        }

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
        if not os.path.exists(_path):
            _path = ROOT_PATH
            session['current_path'] = ROOT_PATH
        return _path

    @route("/command")
    def command(self):
        self.result = {"result": "fail"}

        command = request.args.get('command')
        option = request.args.get('option')

        _path = self.get_current_path()

        if command == 'double_click':
            new_path = os.path.join(_path, option)
            if os.path.exists(new_path) and os.path.isdir(new_path):
                session['current_path'] = new_path
                self.result = {"result" : "refresh"}

        if self.commands.get(command):
            self.commands[command](option)

        return json.dumps(self.result)

    def rename_item(self, option):
        _path = self.get_current_path()
        json_option = json.loads(option)
        origin_file = os.path.join(_path, json_option["origin"])
        new_file = os.path.join(_path, json_option["new"])
        os.rename(origin_file, new_file)
        self.result = {"result": "refresh"}

    def new_folder(self, option):
        _path = self.get_current_path()
        new_path = os.path.join(_path, option)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            self.result = {"result": "refresh"}

    def delete_item(self, option):
        try:
            _path = self.get_current_path()
            items = json.loads(option)
            for item in items:
                _delete_file = os.path.join(_path, item)
                if os.path.isfile(_delete_file):
                    os.remove(_delete_file)
                else:
                    os.rmdir(_delete_file)
        except Exception as e:
            print("delete_item", e)
        self.result = {"result": "refresh"}

    def copy_item(self, option):
        session['copy_path'] = self.get_current_path()
        session['copy_item'] = option
        self.result = {"result": "success"}

    def paste_item(self, _option):
        paste_path = session.get('copy_path')
        paste_items = session.get('copy_item')
        items = json.loads(paste_items)
        _path = self.get_current_path()

        for item in items:
            item_path = os.path.join(paste_path, item)
            new_item = os.path.join(_path, item)
            shutil.copyfile(item_path, new_item)
        self.result = {"result": "refresh"}

    @route("/download")
    def download(self):
        args = request.args
        file_name = args.get('file')
        _path = self.get_current_path()
        full_path = os.path.join(_path, file_name)
        # FIXME: check login
        return send_file(full_path, as_attachment=True)

    @route("/upload", methods=["POST", "GET"])
    def upload(self):
        return render_template('/explorer/upload.html')

    @route("/uploadFile", methods=["POST", "GET"])
    def upload_file(self):
        for f in request.files:
            file = request.files[f]
            _path = self.get_current_path()
            file.save(os.path.join(_path, file.filename))
        return ""