from flask_classful import FlaskView, route
from flask import render_template, session, request, abort, Response, redirect

import re
from urllib.parse import urlparse, urlunparse
import requests

APPROVED_HOSTS = ['125.130.115.231:90/']

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

        return render_template('/proxy/proxy.html', url="http://192.168.29.100:5000/proxy/ref/125.130.115.231:90/trac")

    @route('/ref/<path:url>')
    def root(self, url):
        # If referred from a proxy request, then redirect to a URL with the proxy prefix.
        # This allows server-relative and protocol-relative URLs to work.
        referer = request.headers.get('referer')
        if not referer:
            return Response("Relative URL sent without a a proxying request referal. Please specify a valid proxy host (/p/url)", 400)
        proxy_ref = self.proxied_request_info(referer)
        host = proxy_ref[0]
        redirect_url = "/p/%s/%s%s" % (host, url, ("?" + request.query_string.decode('utf-8') if request.query_string else ""))
        return redirect(redirect_url)

    @route('/ref/<path:url>')
    def proxy(self, url):
        """Fetches the specified URL and streams it out to the client.
        If the request was referred by the proxy itself (e.g. this is an image fetch
        for a previously proxied HTML page), then the original Referer is passed."""
        # Check if url to proxy has host only, and redirect with trailing slash
        # (path component) to avoid breakage for downstream apps attempting base
        # path detection
        url_parts = urlparse('%s://%s' % (request.scheme, url))
        if url_parts.path == "":
            parts = urlparse(request.url)
            return redirect(urlunparse(parts._replace(path=parts.path+'/')))

        r = self.make_request(url, request.method, dict(request.headers), request.form)
        headers = dict(r.raw.headers)
        def generate():
            for chunk in r.raw.stream(decode_content=False):
                yield chunk
        out = Response(generate(), headers=headers)
        out.status_code = r.status_code
        return out

    def make_request(self, url, method, headers={}, data=None):
        url = 'http://%s' % url
        # Ensure the URL is approved, else abort
        #if not self.is_approved(url):
        #    abort(403)

        # Pass original Referer for subsequent resource requests
        referer = request.headers.get('referer')
        if referer:
            proxy_ref = self.proxied_request_info(referer)
            headers.update({ "referer" : "http://%s/%s" % (proxy_ref[0], proxy_ref[1])})

        # Fetch the URL, and stream it back
        return requests.request(method, url, params=request.args, stream=True, headers=headers, allow_redirects=False, data=data)

    def is_approved(self, url):
        """Indicates whether the given URL is allowed to be fetched.  This
        prevents the server from becoming an open proxy"""
        parts = urlparse(url)
        return parts.netloc in APPROVED_HOSTS

    def proxied_request_info(self, proxy_url):
        """Returns information about the target (proxied) URL given a URL sent to
        the proxy itself. For example, if given:
            http://localhost:5000/p/google.com/search?q=foo
        then the result is:
            ("google.com", "search?q=foo")"""
        parts = urlparse(proxy_url)
        if not parts.path:
            return None
        elif not parts.path.startswith('/p/'):
            return None
        matches = re.match('^/ref/([^/]+)/?(.*)', parts.path)
        proxied_host = matches.group(1)
        proxied_path = matches.group(2) or '/'
        proxied_tail = urlunparse(parts._replace(scheme="", netloc="", path=proxied_path))
        print(proxied_host, proxied_tail)
        return ["125.130.115.231:90", "trac"]

