#!/bin/bash
# Copyright 2021 fnwinter@gmail.com

SCRIPT_PATH=$(dirname $(realpath $0))

set -e

pushd $SCRIPT_PATH/.. > /dev/null
  find ./ -type f -name "*.py" ! -path "./venv/*" | xargs pylint --rcfile=$SCRIPT_PATH/pylint.rc
popd > /dev/null

set +e