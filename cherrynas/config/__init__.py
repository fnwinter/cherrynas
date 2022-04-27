# Copyright 2022 fnwinter@gmail.com
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

from config.default import DEFAULT_CONFIG

HOME_PATH = os.path.expanduser('~')
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir))
CONFIG_FOLDER_PATH = os.path.join(HOME_PATH, '.cherrynas')
MODULE_PATH = os.path.join(ROOT_PATH, "cherry_daemon", "modules")
RESOURCE_PATH = os.path.abspath(os.path.join(ROOT_PATH, "resources"))

# ini file
INI_FILE_NAME = "cherrynas.ini"
INI_FILE_PATH = os.path.join(CONFIG_FOLDER_PATH, INI_FILE_NAME)

# log files
LOG_PATH = os.path.join(CONFIG_FOLDER_PATH, "cherrynas.log")
FTP_LOG_FILE_PATH = os.path.join(CONFIG_FOLDER_PATH, "ftp.log")

# database files
ACCOUNT_DB_PATH = os.path.join(CONFIG_FOLDER_PATH, "account.db")

# etc files
DAEMON_LOCK_PATH = os.path.join(CONFIG_FOLDER_PATH, "cherrynas.lock")
SYSTEM_INFO_PATH = os.path.join(CONFIG_FOLDER_PATH, "system_info.json")

"""
Test file path
"""
TEST_CONFIG_READ_PATH = os.path.join(RESOURCE_PATH, "test_read_config.ini")
TEST_CONFIG_WRITE_PATH = os.path.join(RESOURCE_PATH, "test_write_config.ini")

def create_config_folder():
    if not os.path.exists(CONFIG_FOLDER_PATH):
        os.makedirs(CONFIG_FOLDER_PATH)

def create_config():
    try:
        if not os.path.exists(INI_FILE_PATH):
            from config.config import Config
            with Config(open_mode='w') as c:
                c.write_config(DEFAULT_CONFIG)
    except Exception as e:
        print(e)

create_config_folder()
create_config()
