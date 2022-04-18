import os
import subprocess

cherrynas_major_version = 0
cherrynas_minor_version = 0
cherrynas_patch_version = 1

CHERRYNAS_VERSION = f"{cherrynas_major_version}.{cherrynas_minor_version}.{cherrynas_patch_version}"
CHERRYNAS_CODE = 'Nutshell'

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
BUILD_COMMIT_ID = os.path.join(SCRIPT_PATH, "build_id.txt")

def create_commit_log():
    output = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
    commitId = output.strip().decode('utf-8')
    with open(BUILD_COMMIT_ID, "w") as f:
        f.write(commitId)

def GetCommitId():
    with open(BUILD_COMMIT_ID, "r") as f:
        return f.readline()

create_commit_log()