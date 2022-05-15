from flask_classful import FlaskView, route
from flask import render_template, session, request, abort, Response, redirect

from web.common.decorator import login_required

from urllib.parse import urlparse, urlunparse

class ProxyView(FlaskView):
    """
    Proxy Page
    """
    default_methods = ['GET', 'POST']

    @login_required
    def index(self):
        """
        proxy.html
        """
        return render_template('/proxy/proxy.html', url="http://localhost:5000/proxy/ref/ko.wikipedia.org/wiki/%ED%85%8C%EC%8A%A4%ED%8A%B8")

    @route("/static")
    def static(self):
        print("proxy >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", request)