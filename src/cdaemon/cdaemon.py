#!/usr/bin/python3
#
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
"""
cherrynas daemon
"""

import argparse
import daemon
import os
import sys

from daemon import pidfile

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir))
sys.path.append(ROOT_PATH)

from config import DAEMON_LOCK_PATH
from utils.log import get_logger, LogHandler
from utils.process_helper import kill_running_process

from cdaemon.module.loader import ModuleLoader

LOG_MODULE = 'DAEMON'

def start_daemon():
    get_logger(LOG_MODULE).info('start daemon')
    log_file_no = LogHandler().get_file_no()
    if os.path.exists(DAEMON_LOCK_PATH):
        print("already daemon running")
        sys.exit()
    try:
        with daemon.DaemonContext(
                working_directory=ROOT_PATH,
                files_preserve=[log_file_no],
                pidfile=pidfile.TimeoutPIDLockFile(DAEMON_LOCK_PATH)) as context:
            loader = ModuleLoader()
            loader.load_modules()
            loader.launch_modules(context)
            pass
    except Exception as e:
        print(e)

def stop_daemon():
    get_logger(LOG_MODULE).info('stop daemon')
    if not os.path.exists(DAEMON_LOCK_PATH):
        print("no running daemon")
        sys.exit()
    else:
        kill_running_process()

def restart_daemon():
    get_logger(LOG_MODULE).info('restart daemon')
    stop_daemon()
    start_daemon()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CherryNAS Daemon')
    parser.add_argument('--start', action='store_true', help='start the YuriNAS Daemon')
    parser.add_argument('--stop', action='store_true', help='stop the YuriNAS Daemon')
    parser.add_argument('--restart', action='store_true', help='restart the YuriNAS Daemon')
    parser.add_argument('--force', action='store_true', help='delete the lock file')

    args = parser.parse_args()
    try:
        if args.force:
            if os.path.exists(DAEMON_LOCK_PATH):
                os.remove(DAEMON_LOCK_PATH)
        if args.start:
            start_daemon()
        elif args.stop:
            stop_daemon()
        elif args.restart:
            restart_daemon()
        else:
            parser.print_help()
    except Exception as e:
        get_logger(LOG_MODULE).error(e)