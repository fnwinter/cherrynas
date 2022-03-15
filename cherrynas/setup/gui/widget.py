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

SPLITTER = urwid.Divider(' ')

UNDER_LINE_SPLITTER = urwid.Divider('_')

LINE_SPLITTER = urwid.Divider(u'\u2500')

def draw_header():
    """ header """
    version = 'v0.1'
    title = u" [ YuriNas %s ]" % version
    header = urwid.Text(title, align='left')
    header = urwid.AttrWrap(header, 'header')
    return header

def draw_footer():
    """ footer """
    footer = urwid.Text(u" [ F1 SAVE | F2 RESTART DAEMON |"\
        " F3 STOP DAEMON | F4 EXIT | TAB FOCUS MOVE ] ", align='left')
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
