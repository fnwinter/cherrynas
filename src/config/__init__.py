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

HOME_PATH = os.path.expanduser('~')
CONFIG_FOLDER_PATH = os.path.join(HOME_PATH, '.cherrynas')
CONFIG_FILE_NAME = "cherrynas.ini"
CONFIG_FILE_PATH = os.path.join(CONFIG_FOLDER_PATH, CONFIG_FILE_NAME)

LOG_PATH = os.path.join(CONFIG_FOLDER_PATH, "cherrynas.log")
DAEMON_LOCK_PATH = os.path.join(CONFIG_FOLDER_PATH, "cherrynas.lock")
FTP_LOG_FILE_PATH = os.path.join(CONFIG_FOLDER_PATH, "ftp.log")

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir))
MODULE_PATH = os.path.join(ROOT_PATH, "cdaemon", "modules")

RESOURCE_PATH = os.path.abspath(os.path.join(ROOT_PATH, os.path.pardir, "resources"))

"""
Test file path
"""
TEST_CONFIG_READ_PATH = os.path.join(RESOURCE_PATH, "test_read_config.ini")
TEST_CONFIG_WRITE_PATH = os.path.join(RESOURCE_PATH, "test_write_config.ini")

def create_config_folder():
    if not os.path.exists(CONFIG_FOLDER_PATH):
        os.makedirs(CONFIG_FOLDER_PATH)

create_config_folder()
