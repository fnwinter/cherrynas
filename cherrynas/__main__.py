# Copyright 2022 fnwinter@gmail.com

import argparse
import os
import sys
import subprocess

from utils.log import get_logger
from utils.chmod import change_permission

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_MODULE = "main"

def run_daemon(argv):
    DAEMON_SCRIPT_PATH = os.path.join(SCRIPT_PATH, "scripts", "run_daemon.sh")
    subprocess.run([DAEMON_SCRIPT_PATH] + argv, check=True)

def dev_web():
    WEB_SCRIPT_PATH = os.path.join(SCRIPT_PATH, "scripts", "run_web.sh")
    subprocess.run([WEB_SCRIPT_PATH], check=True)

def install():
    INSTALL_SCRIPT_PATH = os.path.join(SCRIPT_PATH, "scripts", "install.sh")
    change_permission(INSTALL_SCRIPT_PATH, "+x")
    subprocess.run([INSTALL_SCRIPT_PATH], check=True)

def setup():
    pass

parser = argparse.ArgumentParser(description='CherryNAS Daemon')
parser.add_argument('--start', action='store_true', help='start the YuriNAS Daemon')
parser.add_argument('--stop', action='store_true', help='stop the YuriNAS Daemon')
parser.add_argument('--restart', action='store_true', help='restart the YuriNAS Daemon')
parser.add_argument('--force', action='store_true', help='delete the lock file')
parser.add_argument('--install', action='store_true', help='install')
parser.add_argument('--setup', action='store_true', help='start setup')
parser.add_argument('--dev-web', action='store_true', help='start flask web only')

args = parser.parse_args()
try:
    if args.start or args.stop or args.restart or args.force:
        run_daemon(sys.argv[1:])
    elif args.install:
        install()
    elif args.setup:
        setup()
    elif args.dev_web:
        dev_web()
    else:
        parser.print_help()
except Exception as e:
    get_logger(LOG_MODULE).error(e)
