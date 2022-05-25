# Copyright 2022 fnwinter@gmail.com

import sys
import os

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(SCRIPT_PATH)

from .web import *
