#!/bin/bash
# Copyright 2021 fnwinter@gmail.com

echo "install cherrynas"

set -e

SCRIPT_PATH=$(dirname $(realpath $0))

pushd $SCRIPT_PATH > /dev/null
  chmod +x ./*
popd

pushd $SCRIPT_PATH/../web > /dev/null
  flask db init
  flask db migrate
  flask db upgrade
popd > /dev/null