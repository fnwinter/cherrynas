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

import os
import logging

from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from config.config import Config
from config import FTP_LOG_FILE_PATH
from utils.log import get_logger

# pylint: disable-msg=too-many-locals
def process_main(context):
    log = get_logger('FTP')
    log.info("FTP Process start")
    logging.basicConfig(filename=FTP_LOG_FILE_PATH, level=logging.INFO)
    config = Config()

    # Authorizer
    from modules.ftp.ftp_authorizer import FTPAuthorizer
    authorizer = FTPAuthorizer()
    try:
        root_enable = config.get_value('FTP', 'ROOT_ENABLE')
        root_path = config.get_value('FTP', 'ROOT_PATH')
        root_account = config.get_value('ACCOUNT', 'EMAIL')
        root_password = config.get_value('ACCOUNT', 'PASSWORD')
        if root_enable and os.path.exists(root_path):
            log.info("root path : %s", root_path)
            authorizer.add_user(root_account, root_password, root_path, perm='elradfmwMT')
    except Exception as e:
        log.error("root error %s", e)

    try:
        anonymouse = config.get_value('FTP', 'ANONYMOUS_ENABLE')
        anonymouse_path = config.get_value('FTP', 'ANONYMOUS_PATH')
        if anonymouse and os.path.exists(anonymouse_path):
            log.info("annoymouse path : %s", anonymouse_path)
            authorizer.add_anonymous(anonymouse_path)
    except Exception as e:
        log.error('anonymouse error %s', e)

    # Handler
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = config.get_value('FTP', 'WELCOME_BANNER').replace('\n', '')
    passive_port = config.get_tuple_value('FTP', 'PASSIVE_PORT')
    if passive_port and len(passive_port) == 2:
        handler.passive_ports = range(passive_port[0], passive_port[1])

    # Server
    server = None
    try:
        _address = config.get_value('FTP', 'ADDRESS')
        _port = config.get_int_value('FTP', 'PORT')
        address = (_address, _port)
        log.info("address : %s, port: %d", _address, _port)
        server = FTPServer(address, handler)
        server.max_cons = config.get_int_value('FTP', 'MAX_CONNECTION')
        server.max_cons_per_ip = config.get_int_value('FTP', 'MAX_CON_PER_IP')
        # pylint: disable=W0212
        context.files_preserve.append(server._fileno)
    except Exception as e:
        log.error("server config error %s", e)

    config.close()

    # start ftp server
    try:
        server.serve_forever()
        log.info("FTP Process stop")
    except Exception as e:
        log.error("FTP server forever error %s", e)