#!/bin/bash
# Copyright 2021 fnwinter@gmail.com

SCRIPT_PATH=$(dirname $(realpath $0))

pushd $SCRIPT_PATH/.. > /dev/null
  find ./ -type f -name "*.py" ! -path "./web/migrations/*" ! -path "./venv/*" | xargs pylint --rcfile=$SCRIPT_PATH/pylint.rc
popd > /dev/null
