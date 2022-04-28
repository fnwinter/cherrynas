import os
import stat

def change_permission(path, permission):
    if os.path.exists(path):
        if ("+x" in permission):
            st = os.stat(path)
            os.chmod(path, st.st_mode | stat.S_IEXEC)
