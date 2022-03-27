#!/usr/bin/env bash
set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE:-$0}" )" && pwd )"

pushd $SCRIPT_DIR/../.. > /dev/null
  export FLASK_APP=cherrynas.web
  export FLASK_DEBUG=1
  flask run --host=0.0.0.0
popd > /dev/null
