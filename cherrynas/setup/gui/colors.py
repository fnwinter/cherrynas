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

colors = [
    ('bg', '', urwid.DARK_GRAY),
    ('title', urwid.LIGHT_BLUE, urwid.LIGHT_GRAY),
    ('header', urwid.BLACK, urwid.LIGHT_CYAN),
    ('footer', urwid.WHITE, urwid.LIGHT_RED),
    ('frame', urwid.LIGHT_GRAY, urwid.DARK_BLUE, ('bold', 'standout')),
    ('dialog', urwid.LIGHT_GRAY, urwid.DARK_BLUE),
    ('button', urwid.LIGHT_GRAY, urwid.DARK_BLUE),
    ('button_content', urwid.BLACK, urwid.LIGHT_CYAN),
    ('button_focus', urwid.LIGHT_RED, urwid.LIGHT_GRAY),
    ('popup_button', urwid.LIGHT_GRAY, urwid.DARK_BLUE),
    ('popup_button_focus', urwid.LIGHT_GRAY, urwid.DARK_RED),
    ('bright', urwid.BLACK, urwid.LIGHT_GRAY, ('bold', 'standout')),
    ('bright_focus', urwid.LIGHT_RED, urwid.LIGHT_GRAY, ('bold', 'standout')),
    ('linebox', urwid.LIGHT_BLUE, urwid.LIGHT_GRAY),
    ('title_label', urwid.WHITE, urwid.DARK_GREEN),
]
