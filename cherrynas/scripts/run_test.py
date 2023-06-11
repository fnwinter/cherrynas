#!/usr/bin/env python3
# Copyright 2021 fnwinter@gmail.com

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
    >>> get_module_name('/module/', 'module_name')
    'module.module_name'
    """
    full_path = os.path.abspath(os.path.join(path, file_name))
    module_path = full_path.replace(ROOT_PATH, '')
    module_name = module_path.replace(os.path.sep, '.')[1:]
    return module_name

def load_python(verbose):
    module_name = None
    test_modules = {}

    for _path, _, _files in os.walk(ROOT_PATH):
        if 'venv' in _path:
            continue
        for _file in _files:
            _file_name, _ext = os.path.splitext(_file)
            if _ext == '.py' and _file_name != '__init__':
                try:
                    module_name = get_module_name(_path, _file_name)
                    module = importlib.import_module(module_name)
                    test_modules[module_name] = module
                except Exception as e:
                    if verbose:
                        print(f"load_python name {module_name}, error {e}")

    return test_modules.values()

def run_test(verbose):
    """
    Run doctest in src/python
    """
    finder = doctest.DocTestFinder(recurse=True)
    runner = doctest.DocTestRunner()

    modules = load_python(verbose)

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
