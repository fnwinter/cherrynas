# Copyright 2019 fnwinter@gmail.com

import re
import urwid

class Screen(urwid.raw_display.Screen):
    """ urwid Screen for WSL """
    def write(self, data):
        data = re.sub("[\x0e\x0f]", "", data)
        super().write(data)
