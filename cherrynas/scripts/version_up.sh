#!/bin/bash
# Copyright 2021 fnwinter@gmail.com

set -e

GIT_TITLE=$(git log -1 --pretty='%s')
SUB='version_up'
if [[ "$GIT_TITLE" == *"$SUB"* ]]; then
  python3 -c 'from config.version import save_version_patch
save_version_patch()'
  NEW_VERSION=`cat ./config/version.txt`
  git config --global user.email "fnwinter@gmail.com"
  git config --global user.name "JungJik Lee"
  git add --all
  git commit -m "version : ${NEW_VERSION}"
  git push origin main
fi