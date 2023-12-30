#!/bin/bash
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
pushd $SCRIPT_DIR

source ./venv/bin/activate

pushd cherrynas
reflex run &
popd

popd
