# Copyright 2019 fnwinter@gmail.com

import hashlib

from datetime import date

def hashed_password(pwd):
    """
    return hashed password
    >>> hashed_password('1234567890')
    'c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646'
    """
    encoded_pwd = pwd.encode()
    return hashlib.sha256(encoded_pwd).hexdigest()

def get_today_hash():
    """
    >>> from utils.hash import get_today_hash
    >>> hash = get_today_hash()
    >>> len(hash)
    32
    """
    md5_hash = hashlib.md5()
    today = date.today()
    md5_hash.update(f"{today}".encode("utf-8"))
    hash_key = md5_hash.hexdigest()
    return hash_key
