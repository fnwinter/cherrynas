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
    # FIXME: delete this duplicated

    size = ''
    try:
        _n_size = os.path.getsize(path)
        if _n_size > 1024 * 1024:
            size = f'{_n_size / 1048576.0} MB'
        elif _n_size > 1024:
            size = f'{_n_size / 1024} KB'
        else:
            size = f'{_n_size} Bytes'

    except os.error:
        size = 'wrong size'
    return size
