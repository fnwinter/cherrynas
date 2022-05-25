# Copyright 2019 fnwinter@gmail.com

import time
import urwid

from gui.screen import Screen
from gui.widget import SPLITTER

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
        title = urwid.BigText("cherrynas", urwid.Thin6x6Font())
        title = urwid.Padding(title, 'center', None)
        title = urwid.AttrMap(title, 'title')
        title = urwid.Filler(title, 'middle', None, 27)
        title = urwid.BoxAdapter(title, 7)

        desc = urwid.Text("Network Attached Storage", align='center')
        version = urwid.Text("v0.1", align='center')
        skip = urwid.Text("Press enter", align='center')
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
