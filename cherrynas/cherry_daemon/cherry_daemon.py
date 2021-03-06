#!/usr/bin/python3
# Copyright 2019 fnwinter@gmail.com
"""
cherrynas daemon
"""

import argparse
import os
import sys
import daemon

from daemon import pidfile

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir))
sys.path.append(ROOT_PATH)

from config import DAEMON_LOCK_PATH
from utils.log import get_logger, LogHandler
from utils.process_helper import kill_running_process

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
            from modules.loader import ModuleLoader
            loader = ModuleLoader()
            loader.load_modules()
            loader.launch_modules(context)
    except Exception as daemon_error:
        get_logger(LOG_MODULE).info(f'error : start daemon {daemon_error}')
    get_logger(LOG_MODULE).info('start daemon exit')

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CherryNAS Daemon')
    parser.add_argument('--start', action='store_true', help='start CherryNas Daemon')
    parser.add_argument('--stop', action='store_true', help='stop CherryNas Daemon')
    parser.add_argument('--restart', action='store_true', help='restart CherryNas Daemon')
    parser.add_argument('--force', action='store_true', help='delete the lock file')
    parser.add_argument('--setup', action='store_true', help='start setup')
    parser.add_argument('--dev-web', action='store_true', help='start flask web only')

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
        get_logger(LOG_MODULE).error(f'error : cherry daemon {e}')
