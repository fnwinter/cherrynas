import hashlib

from datetime import date

def get_today_hash():
    """
    >>> from util.today_hash import get_today_hash
    >>> hash = get_today_hash()
    """
    md5_hash = hashlib.md5()
    md5_hash.update( f"date.today()".encode("utf-8") )
    hash_key = md5_hash.digest()
    return hash_key