#!/usr/bin/env bash
set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE:-$0}" )" && pwd )"

pushd $SCRIPT_DIR/..
  export FLASK_APP=web
  export FLASK_DEBUG=1
  flask run
popd