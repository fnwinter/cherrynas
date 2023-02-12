# Copyright 2022 fnwinter@gmail.com

import os
import subprocess

CHERRYNAS_CODE = 'Nutshell'

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
BUILD_COMMIT_ID = os.path.join(SCRIPT_PATH, "build_id.txt")
VERSION_FILE = os.path.join(SCRIPT_PATH, "version.txt")

def create_commit_id():
    output = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
    commitId = output.strip().decode('utf-8')
    with open(BUILD_COMMIT_ID, "w", encoding="utf8") as f:
        f.write(commitId)

def get_commit_id() -> str:
    with open(BUILD_COMMIT_ID, "r", encoding="utf8") as f:
        return f.readline()

def get_version() -> str:
    with open(VERSION_FILE, 'r', encoding="utf8") as f:
        version_ = f.readline()
        return version_

def save_version_patch():
    version_ = get_version()
    token_ = version_.split('.')
    token_[2] = str(int(token_[2]) + 1)
    print("save_version_patch : " + ".".join(token_))
    with open(VERSION_FILE, 'w', encoding="utf8") as f:
        f.write(".".join(token_))

def get_full_version() -> str:
    return f"{get_version()} - {CHERRYNAS_CODE} - {get_commit_id()}"
