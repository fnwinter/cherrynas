from flask_classful import FlaskView, route
from flask import render_template, redirect

from web.common.decorator import login_required

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
        proxy_url = "/proxy_ref"
        if not proxy_url:
            redirect('/proxy/error')

        return render_template('/proxy/proxy.html', url=proxy_url)

    @route("/error")
    def error(self):
        return render_template('/proxy/proxy_error.html')
