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
import time
import platform
import psutil

#from utils.log import get_logger
#from utils.version import cherrynas_version
cherrynas_version = '0.0.1'

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

def hardware_info():
    """
    Get Hardware Info
    - CPU type
    - RAM size and usage
    - Network usage
    """
    cpu_ = platform.processor()
    ram_ = psutil.virtual_memory()
    print(int(ram_.total / 1024 / 1024))
    return {"cpu": cpu_, "ram": ram_ }
    

def software_info():
    """
    CherryNas Version
    OS name and version
    """
    system_ = platform.system()
    release_ = platform.release()
    version_ = platform.version()
    os_ = f"{system_}-{release_}-{version_}"
    cherrynas_version_ = cherrynas_version
    return {"os": os_, "nas_ver":cherrynas_version_}

def disk_info():
    """
    Disk total size and free size
    """
    

def write_info():
    """
    write info to $HOME/.cherrynas/system_info.json
    
    """

def process_main(_):
    while True:


        time.sleep(60 * 5)

hardware_info()
software_info()
disk_info()
write_info()