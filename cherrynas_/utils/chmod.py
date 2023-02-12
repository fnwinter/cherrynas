# Copyright 2022 fnwinter@gmail.com

import os
import stat

def change_permission(path, permission):
    if os.path.exists(path) and "+x" in permission:
        st = os.stat(path)
        os.chmod(path, st.st_mode | stat.S_IEXEC)
