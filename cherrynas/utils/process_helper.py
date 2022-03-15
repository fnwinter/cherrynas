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
        print("Running child process killed. (PID {})".format(process.pid))
        process.send_signal(SIGKILL)

def kill_running_process():
    if not os.path.exists(DAEMON_LOCK_PATH):
        return
    with open(DAEMON_LOCK_PATH, 'r') as f:
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
