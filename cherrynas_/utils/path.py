# Copyright 2019 fnwinter@gmail.com

import os

def make_sure_path(path):
    """
    If the path does not exist, then create it.
    >>> from config import RESOURCE_PATH
    >>> test_dir = os.path.join(RESOURCE_PATH, 'none')
    >>> make_sure_path(test_dir)
    >>> os.path.exists(test_dir)
    True
    >>> os.rmdir(test_dir)
    """
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
