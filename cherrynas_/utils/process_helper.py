#!/usr/bin/python3
# Copyright 2019 fnwinter@gmail.com

import os
import sys

from signal import SIGKILL
from psutil import Process, NoSuchProcess, process_iter

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir))
sys.path.append(ROOT_PATH)

from config import DAEMON_LOCK_PATH

def kill_child_processes(ppid):
    try:
        parent_process = Process(ppid)
    except NoSuchProcess:
        return

    children_process = parent_process.children(recursive=True)
    for process in children_process:
        print(f"Running child process killed. (PID {process.pid})")
        process.send_signal(SIGKILL)

def kill_running_process():
    if not os.path.exists(DAEMON_LOCK_PATH):
        return
    with open(DAEMON_LOCK_PATH, 'r', encoding="utf8") as f:
        pid = "".join(f.readlines()).strip()
        process_id = int(pid)
        if process_id != 0:
            kill_child_processes(process_id)
            os.kill(process_id, SIGKILL)
    # file is closed, so remove it.
    os.remove(DAEMON_LOCK_PATH)

def kill_process_by_name(name):
    """
    kill all processes filtered by name
    """
    for proc in process_iter():
        if name == proc.name():
            os.kill(proc.pid, SIGKILL)
