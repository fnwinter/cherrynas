# Copyright 2022 fnwinter@gmail.com

import requests

from flask_classful import Response
from flask import redirect, request

def proxy_handler(app):
    @app.route('/')
    def root():
        return redirect('/cherry/')

    @app.route('/<path:url>', methods=["GET", "POST"])
    def proxy(url):
        out = ''
        url_ = ''
        base_url = 'http://localhost'
        try:
            if "proxy_ref" in url:
                url_ = base_url
            else:
                url_ = f"{base_url}/{url}"
            r = requests.request(request.method, url_, stream=True)
            headers = dict(r.raw.headers)
            def generate():
                for chunk in r.raw.stream(decode_content=False):
                    yield chunk
            out = Response(generate(), headers=headers)
            out.status_code = r.status_code
        except Exception as e:
            print('error', e)
        return out
