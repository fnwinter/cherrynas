# Copyright 2019 fnwinter@gmail.com

import os
import subprocess

from utils.log import get_logger

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
WEB_SCRIPT_PATH = os.path.abspath(
    os.path.join(SCRIPT_PATH,
                 os.path.pardir,
                 os.path.pardir,
                 os.path.pardir,
                 "scripts",
                 "run_web.sh"))

def process_main(_):
    log = get_logger('web')
    log.info(WEB_SCRIPT_PATH)
    subprocess.check_output(WEB_SCRIPT_PATH)
