# Copyright 2019 fnwinter@gmail.com
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

import urwid

from base.gui.widget import SPLITTER
from utils.log import get_logger

class BaseTextUI():
    """ Base Text UI class """
    contents = []
    config_data = {}
    module_name = ''
    screen = None

    def __init__(self, module_name):
        self.module_name = module_name
        self.log = get_logger(module_name)

    @staticmethod
    def draw_title(title):
        _title = urwid.AttrWrap(urwid.Text(title, align='left'), 'title_label')
        _line = urwid.AttrWrap(urwid.Divider(u'\u2500'), 'title_label')
        return [_line, _title, _line, SPLITTER]

    def set_config(self, config_data):
        _config = {}
        for c in config_data:
            if self.module_name in c:
                _config[c] = config_data[c]
        self.config_data.update(_config)

    def get_config(self):
        return self.config_data

    def get_config_value(self, key):
        value = self.config_data.get(key)
        if type(value).__name__ == 'bool':
            return value
        return "%s" % value

    def get_focus_order(self):
        index = 0
        focus_order = []
        for widget in self.contents:
            widget_name = str(widget.__class__)
            if widget_name.find('Edit') > 0:
                focus_order.append(index)
            elif widget_name.find('CheckBox') > 0:
                focus_order.append(index)
            elif widget_name.find('Button') > 0:
                focus_order.append(index)
            elif widget_name.find('FocusAttrWrap') > 0:
                focus_order.append(index)
            index += 1
        return focus_order

    def set_screen(self, screen):
        self.screen = screen

    def clear_screen(self):
        if self.screen:
            self.screen.clear()

    def save_config_data(self, widget, data):
        if hasattr(widget, 'get_name'):
            name = widget.get_name()
            self.config_data[name] = data
