# Copyright 2019 fnwinter@gmail.com

import urwid

from gui.widget import SPLITTER

class BaseTextUI():
    """ Base Text UI class """
    contents = []
    config_data = {}
    module_name = ''
    screen = None

    def __init__(self, module_name):
        self.module_name = module_name

    @staticmethod
    def draw_title(title):
        _title = urwid.AttrWrap(urwid.Text(title, align='left'), 'title_label')
        _line = urwid.AttrWrap(urwid.Divider('\u2500'), 'title_label')
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
