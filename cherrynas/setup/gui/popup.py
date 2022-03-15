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

from base.gui.screen import Screen
from base.gui.colors import colors
from base.gui.widget import LINE_SPLITTER
from base.gui.widget import draw_header, draw_footer

class BasePopup:
    """ Base Popup Class """
    def __init__(self):
        self.screen = Screen()
        self.title = None
        self.messages = []
        self.buttons = []
        self.current_focus_pos = 0
        self.grid_buttons = None
        self.return_value = None

    def show(self):
        title = urwid.Text(self.title, align='left')

        messages = []
        for message in self.messages:
            messages.append(urwid.Text(message, align='center'))

        self.grid_buttons = urwid.GridFlow(self.buttons, 10, 3, 1, 'center')
        self.grid_buttons.set_focus(0)

        pile = urwid.Pile(
            [title, LINE_SPLITTER] + messages +
            [LINE_SPLITTER, self.grid_buttons])

        linebox = urwid.LineBox(pile)
        linebox = urwid.AttrMap(linebox, 'linebox')
        linebox = urwid.Padding(linebox, width=60, align='center')
        linebox = urwid.Filler(linebox, 'middle')

        frame = urwid.Frame(linebox,
                            draw_header(),
                            draw_footer())
        frame = urwid.AttrWrap(frame, 'dialog')

        loop = urwid.MainLoop(
            frame, colors, self.screen,
            unhandled_input=self.unhandled_input)
        loop.run()

        return self.return_value

    def unhandled_input(self, key):
        if str(key) == 'tab':
            self.current_focus_pos += 1
            if self.current_focus_pos > len(self.buttons) - 1:
                self.current_focus_pos = 0
            self.grid_buttons.set_focus(self.current_focus_pos)

    def on_press(self, _, user_data):
        self.return_value = user_data
        raise urwid.ExitMainLoop()

class YesNoPopup(BasePopup):
    """ Yes or No Popup """
    def __init__(self, title=u'# Popup #', messages=None):
        BasePopup.__init__(self)
        self.title = title
        self.messages = messages if messages else []
        yes = urwid.Button(u'Yes', on_press=self.on_press, user_data='yes')
        yes = urwid.AttrWrap(yes, 'popup_button', 'popup_button_focus')
        no = urwid.Button(u'No', on_press=self.on_press, user_data='no')
        no = urwid.AttrWrap(no, 'popup_button', 'popup_button_focus')
        self.buttons = [yes, no]
