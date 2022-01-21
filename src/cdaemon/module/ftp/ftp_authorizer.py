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

from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed

from utils.hash import hashed_password
from utils.log import get_logger

class FTPAuthorizer(DummyAuthorizer):
    """
    Use hashed password
    """
    def __init__(self):
        super().__init__()
        self.log = get_logger('FTPAuthorizer')

    def validate_authentication(self, username, password, handler):
        self.log.info('request to auth for %s', username)
        _password = hashed_password(password)
        try:
            if self.user_table[username]['pwd'] != _password:
                raise KeyError
        except KeyError:
            raise AuthenticationFailed