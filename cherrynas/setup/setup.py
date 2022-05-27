#!/usr/bin/python3
# Copyright 2019 fnwinter@gmail.com

from collections import deque

import os
import sys
import urwid

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH = os.path.join(SCRIPT_PATH, os.path.pardir)
sys.path.append(ROOT_PATH)

from gui.splash import Splash
from gui.screen import Screen
from gui.colors import colors
from gui.popup import YesNoPopup
from gui.widget import draw_header, draw_footer

from account.text_ui import TextUI as accountUI
#from ftp.text_ui import TextUI as ftpUI
from config.config import Config

class CherryNasUI():
    """ CharryNas Setup TextUI """
    def __init__(self):
        self.screen = Screen()
        self.list_walker = urwid.SimpleFocusListWalker([])
        self.column = None
        self.instance = None
        self.focus_order = deque(['left', 'right'])
        self.global_config_data = self.load_config()
        print("global_config", self.global_config_data)
        self.modules = [
            accountUI,
            #ftpUI
        ]

    def load_config(self):
        try:
            with Config() as config:
                return config.get_config_data()
        except Exception as e:
            self.log.error("load config %s", e)
        return {}

    def draw_left(self):
        """ draw left column menu buttons """
        buttons = []
        for module in sorted(self.modules, key=lambda module: module.get_label()):
            label = module.get_label() if hasattr(module, 'get_label') else "Unknown"
            button = urwid.Button(label, on_press=self.on_press_left_button, user_data=module)
            button = urwid.AttrWrap(button, 'button', focus_attr='button_focus')
            buttons.append(button)
        return urwid.LineBox(urwid.ListBox(buttons))

    def on_press_left_button(self, _, module):
        """ load right column module when left menu pressed """
        # update previous setup config data
        self.update_config_data()

        if module:
            self.instance = module()
            if hasattr(self.instance, 'set_config'):
                self.instance.set_config(self.global_config_data)
            if hasattr(self.instance, 'set_screen'):
                self.instance.set_screen(self.screen)
            if hasattr(self.instance, 'get_focus_order')\
                and hasattr(self.instance, 'draw_text_ui'):
                self.list_walker.clear()
                self.list_walker.extend(self.instance.draw_text_ui())
                self.focus_order = deque(
                    ['left', 'right'] + self.instance.get_focus_order())
            return True
        return True

    def draw_right(self):
        """ draw right column ui """
        return urwid.LineBox(urwid.ListBox(self.list_walker))

    def show_gui(self):
        """ show text ui """
        menu = self.draw_left()
        content = self.draw_right()
        left_column_width = 35
        self.column = urwid.Columns([(left_column_width, menu), (content)])

        frame = urwid.Frame(self.column,
                            draw_header(),
                            draw_footer())
        frame = urwid.AttrWrap(frame, 'frame')

        urwid.MainLoop(frame, colors, self.screen,
                       unhandled_input=self.unhandled_input_key).run()

    def unhandled_input_key(self, key):
        key_str = str(key)
        if key_str == 'tab':
            self.focus_move()
        elif key_str == 'f1':
            self.save_config()
        elif key_str == 'f2':
            raise urwid.ExitMainLoop()

    def update_config_data(self):
        """ update modules config data """
        if self.instance and hasattr(self.instance, 'get_config'):
            self.global_config_data.update(self.instance.get_config())

    def save_config(self):
        """ save config file """
        result = YesNoPopup(
            title='# Yes or No? #',
            messages=["Do you want to save current config?"]).show()
        self.screen.clear()
        if result == 'no':
            return

        self.update_config_data()

        try:
            with Config(open_mode='w+') as config:
                config.write_config(self.global_config_data)
        except Exception as e:
            print("save config : ", e)

    def focus_move(self):
        self.focus_order.rotate(-1)
        pos = self.focus_order[0]
        if pos == 'left':
            self.column.set_focus_column(0)
        elif pos == 'right':
            self.column.set_focus_column(1)
            if len(self.focus_order) != 2:
                self.focus_order.rotate(-1)
            pos = self.focus_order[0]
            if pos in self.list_walker.positions():
                self.list_walker.set_focus(pos)
        else:
            if pos in self.list_walker.positions():
                self.list_walker.set_focus(pos)

if __name__ == '__main__':
    # show splash
    Splash().show_splash()
    # show cherrynas gui
    CherryNasUI().show_gui()
