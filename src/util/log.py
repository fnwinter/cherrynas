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

import logging

from logging.handlers import RotatingFileHandler

LOG_FILE_PATH = "."

class LogHandler():
    """
    Log Handler (Singleton)
    """
    log_handler = None
    def __new__(cls):
        """
        >>> from utils.log import LogHandler
        >>> log1 = LogHandler()
        >>> log2 = LogHandler()
        >>> log1 is log2
        True
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super(LogHandler, cls).__new__(cls)
        return cls.instance

    def get_handler(self, log_file=LOG_FILE_PATH):
        """
        >>> from utils.log import LogHandler
        >>> LogHandler().close() # close the previous log file due to singleton
        >>> import os
        >>> from base.path.path import TEST_RESOURCE_PATH
        >>> test_file_path = os.path.join(TEST_RESOURCE_PATH, 'test.log')
        >>> log1 = LogHandler().get_handler(test_file_path)
        >>> log2 = LogHandler().get_handler(test_file_path)
        >>> log1 is log2
        True
        """
        if self.log_handler:
            return self.log_handler
        self.log_handler = RotatingFileHandler(
            log_file,
            mode="a", maxBytes=1024*1024,
            backupCount=10, encoding='utf8')
        formatter = logging.Formatter("%(asctime)s > %(name)s [%(levelname)s] - %(message)s")
        self.log_handler.setFormatter(formatter)
        return self.log_handler

    def close(self):
        """ close log file """
        if self.log_handler:
            self.log_handler.close()
            self.log_handler = None

    def get_file_no(self):
        """ return log file no for daemon context """
        if self.log_handler:
            return self.log_handler.stream.fileno()
        return -1

def get_logger(module_name, log_file=LOG_FILE_PATH, level=logging.DEBUG):
    """
    get logger with module name
    - this function returns logger
    >>> import os
    >>> from base.path.path import TEST_RESOURCE_PATH
    >>> from utils.log import get_logger
    >>> test_file_path = os.path.join(TEST_RESOURCE_PATH, 'test.log')
    >>> log = get_logger('test_module', test_file_path)
    >>> log.debug('debug log')
    >>> log.info('info log')
    >>> log.warning('warning log')
    >>> log.error('error log')
    >>> log.critical('critical log')
    >>> with open(test_file_path) as f:
    ...     list(map(lambda x: print(x[x.find('>'):-1]),f.readlines()))
    > test_module [DEBUG] - debug log
    > test_module [INFO] - info log
    > test_module [WARNING] - warning log
    > test_module [ERROR] - error log
    > test_module [CRITICAL] - critical log
    [None, None, None, None, None]
    >>> os.remove(test_file_path)
    """
    assert module_name, "no module name"

    log_handler = LogHandler().get_handler(log_file)

    logger = logging.getLogger(module_name)
    logger.addHandler(log_handler)
    logger.setLevel(level)

    return logger