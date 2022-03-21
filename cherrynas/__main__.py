import argparse
import os
import subprocess

from cherry_daemon import *
from utils.log import get_logger, LogHandler

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_MODULE = "main"

def setup():
    pass

def dev_web():
    WEB_SCRIPT_PATH = os.path.join(SCRIPT_PATH, "scripts", "run_web.sh")
    subprocess.run([WEB_SCRIPT_PATH])

parser = argparse.ArgumentParser(description='CherryNAS Daemon')
parser.add_argument('--start', action='store_true', help='start the YuriNAS Daemon')
parser.add_argument('--stop', action='store_true', help='stop the YuriNAS Daemon')
parser.add_argument('--restart', action='store_true', help='restart the YuriNAS Daemon')
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
    elif args.setup:
        setup()
    elif args.dev_web:
        dev_web()
    else:
        parser.print_help()
except Exception as e:
    get_logger(LOG_MODULE).error(e)
