#!/bin/bash
# Copyright 2021 fnwinter@gmail.com

set -e

SCRIPT_PATH=$(dirname $(realpath $0))

pushd $SCRIPT_PATH/../cherry_daemon > /dev/null
  python3 ./cherry_daemon.py "$@"
popd > /dev/null
