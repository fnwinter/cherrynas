# Copyright 2019 fnwinter@gmail.com

import urwid

SPLITTER = urwid.Divider(' ')

UNDER_LINE_SPLITTER = urwid.Divider('_')

LINE_SPLITTER = urwid.Divider('\u2500')

def draw_header():
    """ header """
    version = 'v0.1'
    title = f" [ cherrynas {version} ]"
    header = urwid.Text(title, align='left')
    header = urwid.AttrWrap(header, 'header')
    return header

def draw_footer():
    """ footer """
    footer = urwid.Text(" [ F1 SAVE | F2 EXIT | TAB FOCUS MOVE ] ", align='left')
    footer = urwid.AttrWrap(footer, 'footer')
    return footer

class FocusAttrWrap(urwid.AttrWrap):
    """ AttrWrap for focusable widget """
    focusable = True

class NamedEdit(urwid.Edit):
    """ named edit widget for saving config data """
    name = None
    def __init__(self, *args, **kwargs):
        if kwargs.get('name'):
            self.name = kwargs.get('name')
            del kwargs['name']
        if kwargs.get('callback'):
            call_back = kwargs.get('callback')
            urwid.connect_signal(self, 'change', call_back)
            del kwargs['callback']
        super().__init__(*args, **kwargs)
    def get_name(self):
        return self.name

class NamedCheckBox(urwid.CheckBox):
    """ named checkbox widget for saving config data """
    name = None
    def __init__(self, *args, **kwargs):
        if kwargs.get('name'):
            self.name = kwargs.get('name')
            del kwargs['name']
        super().__init__(*args, **kwargs)
    def get_name(self):
        return self.name
