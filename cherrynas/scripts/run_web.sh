#!/bin/bash
# Copyright 2021 fnwinter@gmail.com

set -e

SCRIPT_PATH=$(dirname $(realpath $0))

pushd $SCRIPT_PATH/.. > /dev/null
  python3 ./web/app.py
popd > /dev/null
