# Copyright 2022 fnwinter@gmail.com

import os

def get_file_size(path):
    """
    >>> from config import RESOURCE_PATH
    >>> import os
    >>> text_file = os.path.join(RESOURCE_PATH, "text_file.txt")
    >>> get_file_size(text_file)
    '22 Bytes'
    """

    size = ''
    try:
        _n_size = os.path.getsize(path)
        if _n_size > 1024 * 1024:
            size = '%.2f MB' % (_n_size / 1048576.0)
        elif _n_size > 1024:
            size = '%d KB' % (_n_size / 1024)
        else:
            size = '%d Bytes' % _n_size

    except os.error:
        size = 'wrong size'
    return size
