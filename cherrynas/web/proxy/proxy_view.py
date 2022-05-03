from flask_classful import FlaskView, route
from flask import render_template, session, request, abort, Response, redirect

import re
from urllib.parse import urlparse, urlunparse
import requests

APPROVED_HOSTS = set(["google.com", "www.google.com", "yahoo.com", "fnwinter.github.io", "ko.wikipedia.org"])
CHUNK_SIZE = 1024

# https://gist.github.com/gear11/8006132

class ProxyView(FlaskView):
    """
    Proxy Page
    """
    default_methods = ['GET', 'POST']

    def index(self):
        """
        proxy.html
        """
        who = None
        if session.get('nick_name'):
            who = f"{session.get('nick_name')}"
        elif session.get('email'):
            who = f"{session.get('email')}"
        else:
            return redirect('/login')

        return render_template('/proxy/proxy.html', url="http://127.0.0.1:5000/proxy/ref/ko.wikipedia.org/wiki/%ED%85%8C%EC%8A%A4%ED%8A%B8")

    @route('/ref/<path:url>')
    def proxy(self, url):
        """Fetches the specified URL and streams it out to the client.
        If the request was referred by the proxy itself (e.g. this is an image fetch for
        a previously proxied HTML page), then the original Referer is passed."""
        r = self.get_source_rsp(url)
        print(url)
        headers = dict(r.headers)
        def generate():
            for chunk in r.raw.stream(decode_content=False):
                yield chunk
        return Response(generate(), headers = headers)

    def get_source_rsp(self, url):
        url = 'http://%s' % url
        # Ensure the URL is approved, else abort
        if not self.is_approved(url):
            abort(403)
        # Pass original Referer for subsequent resource requests
        proxy_ref = self.proxy_ref_info(request)
        headers = { "Referer" : "http://%s/%s" % (proxy_ref[0], proxy_ref[1])} if proxy_ref else {}
        req = requests.get(url, stream=True , params = request.args, headers=headers)
        print(req)
        return req

    def is_approved(self, url):
        """Indicates whether the given URL is allowed to be fetched.  This
        prevents the server from becoming an open proxy"""
        host = self.split_url(url)[1]
        print(host)
        return host in APPROVED_HOSTS

    def split_url(self, url):
        """Splits the given URL into a tuple of (protocol, host, uri)"""
        proto, rest = url.split(':', 1)
        rest = rest[2:].split('/', 1)
        host, uri = (rest[0], rest[1]) if len(rest) == 2 else (rest[0], "")
        return (proto, host, uri)

    def proxy_ref_info(self, request):
        """Parses out Referer info indicating the request is from a previously proxied page.
        For example, if:
            Referer: http://localhost:8080/p/google.com/search?q=foo
        then the result is:
            ("google.com", "search?q=foo")
        """
        return ("ko.wikipedia.org","/wiki/%ED%85%8C%EC%8A%A4%ED%8A%B8")
        ref = request.headers.get('referer')
        if ref:
            _, _, uri = self.split_url(ref)
            if uri.find("/") < 0:
                return None
            first, rest = uri.split("/", 1)
            if first in "pd":
                parts = rest.split("/", 1)
                r = (parts[0], parts[1]) if len(parts) == 2 else (parts[0], "")
                return r
        return None

