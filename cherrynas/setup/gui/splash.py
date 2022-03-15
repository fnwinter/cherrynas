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

import time
import urwid

from base.gui.screen import Screen
from base.gui.widget import SPLITTER

class Splash():
    """ YuriNas Text UI Splash """
    def __init__(self):
        self.palette = [
            ('background', '', 'dark gray'),
            ('title', urwid.LIGHT_RED, urwid.LIGHT_GRAY),
            ('linebox', urwid.LIGHT_BLUE, urwid.LIGHT_GRAY)]
        self.screen = Screen()

    @staticmethod
    def exit_by_key(key):
        if key in 'enter':
            raise urwid.ExitMainLoop()

    @staticmethod
    def time_out(w, d):
        raise urwid.ExitMainLoop()

    def show_splash(self):
        title = urwid.BigText(u"yurinas", urwid.Thin6x6Font())
        title = urwid.Padding(title, 'center', None)
        title = urwid.AttrMap(title, 'title')
        title = urwid.Filler(title, 'middle', None, 27)
        title = urwid.BoxAdapter(title, 7)

        desc = urwid.Text(u"Network Attached Storage", align='center')
        version = urwid.Text(u"v0.1", align='center')
        skip = urwid.Text(u"Press enter", align='center')
        pile = urwid.Pile(
            [title, desc, SPLITTER, version, SPLITTER, skip, SPLITTER])

        linebox = urwid.LineBox(pile)
        linebox = urwid.AttrMap(linebox, 'linebox')
        linebox = urwid.Padding(linebox, width=80, align='center')

        fill = urwid.Filler(linebox, 'middle')
        bgcolor = urwid.AttrMap(fill, 'background')
        loop = urwid.MainLoop(bgcolor, self.palette,
                              self.screen, unhandled_input=Splash.exit_by_key)
        loop.set_alarm_at(time.time() + 5, Splash.time_out)
        loop.run()
