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
import importlib

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir, os.path.pardir))
DAEDMON_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir))

from config import MODULE_PATH
from utils.log import get_logger

class ModuleLoader():
    """
    load modules in cdaemon/modules
    """
    def __init__(self, module_path=MODULE_PATH, root_path=DAEDMON_PATH):
        """
        >>> ml = ModuleLoader(root_path=ROOT_PATH)
        >>> modules = ml.load_modules()
        """
        self.modules = {}
        self.root_path = root_path
        self.module_path = module_path
        self.log = get_logger('module_loader')

    def get_module_name(self, path, file_name):
        """
        get module name
        >>> import os
        >>> ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir, os.path.pardir))
        >>> ml = ModuleLoader(root_path=ROOT_PATH)
        >>> ml.root_path = '/root'
        >>> ml.get_module_name('/root/module/', 'module_name')
        'module.module_name'
        """
        full_path = os.path.abspath(os.path.join(path, file_name))
        module_path = full_path.replace(self.root_path, '')
        module_name = module_path.replace(os.path.sep, '.')[1:]
        return module_name

    def get_daemon_module_names(self):
        """
        get daemon module
        >>> import os
        >>> ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir, os.path.pardir))
        >>> ml = ModuleLoader(root_path=ROOT_PATH)
        >>> modules = ml.load_modules()
        >>> daemon_modules = ml.get_daemon_module_names()
        >>> 'cdaemon.modules.dummy.dummy' in daemon_modules
        True
        """
        daemon_modules = []
        for module in self.modules.values():
            if getattr(module, 'process_main', False):
                daemon_modules.append(module.__name__)
        return daemon_modules

    def load_modules(self):
        """
        load modules
        >>> import os
        >>> ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir, os.path.pardir))
        >>> ml = ModuleLoader(root_path=ROOT_PATH)
        >>> _modules = ml.load_modules()
        >>> _module_names = [m.__name__ for m in _modules]
        >>> 'cdaemon.modules.dummy.dummy' in _module_names
        True
        """
        module_name = None
        try:
            for _path, _, _files in os.walk(self.module_path):
                for _file in _files:
                    _file_name, _ext = os.path.splitext(_file)
                    if _file_name in ['__init__', 'loader', 'module_process']:
                        continue
                    if _ext == '.py':
                        module_name = self.get_module_name(_path, _file_name)
                        module = importlib.import_module(module_name)
                        self.modules[module_name] = module
        except Exception as e:
            self.log.error("load_modules name %s, error %s", module_name, e)
        return self.modules.values()

    def launch_modules(self, context=None):
        """
        launch daemon process
        """
        try:
            from modules.module_process import ModuleProcess
            process_list = []
            daemon_module_names = self.get_daemon_module_names()
            for name in daemon_module_names:
                module = self.modules[name]
                process = ModuleProcess(name, context, module.process_main)
                process.start()
                process_list.append(process)

            for process in process_list:
                process.join()
        except Exception as e:
            self.log("launch_modules %s", e)
