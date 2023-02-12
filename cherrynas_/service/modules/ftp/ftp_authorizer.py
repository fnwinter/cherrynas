# Copyright 2019 fnwinter@gmail.com

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
            raise AuthenticationFailed from KeyError
