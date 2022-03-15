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

import hashlib

from datetime import date

def hashed_password(pwd):
    """
    return hashed password
    >>> hashed_password('1234567890')
    'c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646'
    """
    encoded_pwd = pwd.encode()
    return hashlib.sha256(encoded_pwd).hexdigest()

def get_today_hash():
    """
    >>> from utils.hash import get_today_hash
    >>> hash = get_today_hash()
    >>> len(hash)
    32
    """
    md5_hash = hashlib.md5()
    md5_hash.update(f"date.today()".encode("utf-8"))
    hash_key = md5_hash.hexdigest()
    return hash_key
