#!/usr/bin/env bash
# Copyright 2021 fnwinter@gmail.com

set -e

SCRIPT_PATH=$(dirname $(realpath $0))

python3 $SCRIPT_PATH/run_test.py
