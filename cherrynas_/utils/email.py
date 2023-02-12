# Copyright 2022 fnwinter@gmail.com

import re

"""
If email is valid, return True
if Not, return False
"""
def validate_email(email) -> bool:
    re_rule = r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(re_rule, email):
        return True
    return False
