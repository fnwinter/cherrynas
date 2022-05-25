# Copyright 2019 fnwinter@gmail.com

import os
import sys
import time
import json
import platform
import psutil

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(SCRIPT_PATH, os.path.pardir, os.path.pardir,os.path.pardir))

from config.version import get_full_version
from config import SYSTEM_INFO_PATH
from utils.unit import HumanReadByte
from utils.log import get_logger

def hardware_info():
    """
    Get Hardware Info
    - CPU type
    - RAM size and usage
    - Network usage
    """
    cpu_ = platform.processor()
    ram_ = psutil.virtual_memory()
    ram_total_ = HumanReadByte(ram_.total)
    ram_available_ = HumanReadByte(ram_.available)
    ram_used_ = HumanReadByte(ram_.used)
    ram_free_ = HumanReadByte(ram_.free)
    load_ = psutil.getloadavg()
    cpu_count_ = psutil.cpu_count()

    return {"cpu": cpu_, "cpu_count": cpu_count_, "cpu_load": load_,
        "ram_total": ram_total_, \
        "ram_available" : ram_available_, "ram_used": ram_used_,\
        "ram_free": ram_free_}

def software_info():
    """
    CherryNas Version
    OS name and version
    """
    system_ = platform.system()
    release_ = platform.release()
    os_ = f"{system_}-{release_}"
    cherrynas_version_ = get_full_version()

    return {"os": os_, "cherrynas version":cherrynas_version_}

def disk_info():
    """
    Disk total size and free size
    """
    disk = psutil.disk_usage('/')

    return {"total": disk.total, "used": disk.used, "free": disk.free, "usage": disk.percent}

def write_info():
    """
    write info to $HOME/.cherrynas/system_info.json
    """
    hw_ = hardware_info()
    sw_ = software_info()
    disk_ = disk_info()
    system_ = { "hw": hw_, "sw": sw_, "disk": disk_}
    with open(SYSTEM_INFO_PATH, "w") as json_file:
        json.dump(system_, json_file)

def process_main(_):
    log = get_logger('system_info')
    while True:
        log.info("collect system info")
        # update system info per 10 mins
        write_info()
        time.sleep(60 * 10)
