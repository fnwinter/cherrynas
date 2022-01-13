#!/usr/bin/env python3
# Copyright 2021 fnwinter@gmail.com
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

import doctest
import sys
import importlib
import os

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir))
sys.path.append(ROOT_PATH)

def get_module_name(path, file_name):
    """
    get module name
    >>> ml = ModuleLoader()
    >>> ml.root_path = '/root'
    >>> ml.get_module_name('/root/module/', 'module_name')
    'module.module_name'
    """
    full_path = os.path.abspath(os.path.join(path, file_name))
    module_path = full_path.replace(ROOT_PATH, '')
    module_name = module_path.replace(os.path.sep, '.')[1:]
    return module_name

def load_python(self):
    module_name = None
    modules = {}
    try:
        for _path, _, _files in os.walk(ROOT_PATH):
            for _file in _files:
                _file_name, _ext = os.path.splitext(_file)
                if _ext == '.py' and _file_name != '__init__':
                    module_name = get_module_name(_path, _file_name)
                    module = importlib.import_module(module_name)
                    modules[module_name] = module
    except Exception as e:
        print(f"load_python name {module_name}, error {e}")
    return modules.values()

def run_test(verbose):
    """
    Run doctest in src/python
    """
    finder = doctest.DocTestFinder(recurse=True)
    runner = doctest.DocTestRunner()

    modules = load_python(ROOT_PATH)
    
    for module in modules:
        for test in finder.find(module):
            runner.run(test)

    result = runner.summarize(verbose)
    print("- Test Result -\n")
    print(result)
    print('')
    if result.failed != 0:
        print("failed tests exists.")
        sys.exit(1)

if __name__ == "__main__":
    run_test('-v' in sys.argv)