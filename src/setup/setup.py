#!/usr/bin/python3
#
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

from collections import deque

import os
import urwid

from base.config.config import Config
from base.gui.splash import Splash
from base.gui.screen import Screen
from base.gui.colors import colors
from base.gui.popup import YesNoPopup
from base.gui.widget import draw_header, draw_footer
from base.path.path import ROOT_PATH, TEXTUI_LOG_FILE_PATH
from modules.loader import ModuleLoader
from utils.log import get_logger

class YuriNasUI():
    """ YuriNas Setup TextUI """
    def __init__(self):
        self.log = get_logger('TEXT_UI', log_file=TEXTUI_LOG_FILE_PATH)
        self.screen = Screen()
        self.list_walker = urwid.SimpleFocusListWalker([])
        self.column = None
        self.instance = None
        self.focus_order = deque(['left', 'right'])
        self.global_config_data = self.load_config()
        self.modules = self.load_tui_modules()

    def load_config(self):
        try:
            with Config() as config:
                return config.get_config_data()
        except Exception as e:
            self.log.error("load config %s", e)
        return {}

    def load_tui_modules(self):
        """ load text ui modules """
        try:
            self.log.info('load text ui modules')
            module_loader = ModuleLoader()
            module_loader.load_modules()
            return module_loader.get_text_ui_modules()
        except Exception as e:
            self.log.error("fail to load modules : %s", e)
            assert False, "fail to load modules"

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
            self.restart_daemon()
        elif key_str == 'f3':
            self.stop_daemon()
        elif key_str == 'f4':
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
            self.log.error("fail to save the config file : %s", e)

    def restart_daemon(self):
        """ restart daemon """
        try:
            self.log.info("restart daemon")
            daemon_path = os.path.join(ROOT_PATH, 'yurinas-daemon.py')
            self.log.info("daemon path : %s", daemon_path)
            command = "python3 %s --restart --force" % daemon_path
            os.system(command)
        except Exception as e:
            self.log.error("fail to restart daemon : %s", e)

    def stop_daemon(self):
        self.log.info("stop daemon")

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
    # show yurinas gui
    YuriNasUI().show_gui()
