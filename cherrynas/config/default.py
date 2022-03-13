# Copyright 2019 fnwinter@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

DEFAULT_CONFIG = {
    # ACCOUNT
    'ACCOUNT_EMAIL': 'admin@cherrynas',
    'ACCOUNT_PASSWORD': '1234567890',

    # FTP
    'FTP_ROOT_ENABLE': True,
    'FTP_ROOT_PATH': '/ftp/path/here',
    'FTP_ANONYMOUS_ENABLE': True,
    'FTP_ANONYMOUS_PATH': '/ftp/path/here',
    'FTP_PASSIVE_PORT': "60000, 65535",
    'FTP_ADDRESS': '127.0.0.1',
    'FTP_PORT': '21',
    'FTP_MAX_CONNECTION': '10',
    'FTP_MAX_CON_PER_IP': '2',
    'FTP_WELCOME_BANNER': '\nWelcome! cherrynas FTP server.\n',
}

def load_default(section):
    """
    >>> load_default('ACCOUNT').get('ACCOUNT_EMAIL')
    'admin@cherrynas'
    >>> load_default('FTP').get('FTP_ROOT_ENABLE')
    True
    """
    config = {}
    for d in DEFAULT_CONFIG:
        if section in d:
            config.update({d:DEFAULT_CONFIG.get(d)})
    return config
