#!/bin/bash
# Copyright 2021 fnwinter@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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