# Copyright 2019 fnwinter@gmail.com

import urwid

from gui.widget import SPLITTER, LINE_SPLITTER, FocusAttrWrap
from gui.widget import NamedCheckBox, NamedEdit
from gui.browse import DirectoryBrowser
from gui.base_text_ui import BaseTextUI

class TextUI(BaseTextUI):
    """
    Text UI for FTP
    """
    def __init__(self):
        super().__init__('FTP')
        self.contents = None
        self.root_path = None
        self.root_button = None
        self.enable_anonymous = None
        self.enable_root = None
        self.anonymous_button = None
        self.anonymous_path = None
        self.address = None
        self.port = None
        self.passive_port = None
        self.max_connection = None
        self.max_connection_per_ip = None
        self.banner = None

    @staticmethod
    def get_label():
        return "FTP"

    def draw_text_ui(self):
       #admin
        self.enable_root = NamedCheckBox(
            "Enable FTP server",
            name='FTP_ROOT_ENABLE',
            state=self.get_config_value('FTP_ROOT_ENABLE'),
            on_state_change=self.callback)
        self.root_path = NamedEdit(
            '    Root path : ', name='FTP_ROOT_PATH', align='left',
            edit_text=self.get_config_value('FTP_ROOT_PATH'),
            callback=self.callback)
        self.root_button = FocusAttrWrap(
            urwid.Button("  Press to select folder",
                         on_press=self.callback, user_data='admin_button'),
            'button_content', focus_attr='button_focus')

        #anonymous
        self.enable_anonymous = NamedCheckBox(
            "Enable anonymous user",
            name='FTP_ANONYMOUS_ENABLE',
            state=self.get_config_value('FTP_ANONYMOUS_ENABLE'),
            on_state_change=self.callback)
        self.anonymous_path = NamedEdit(
            '    Anonymous path : ',
            name='FTP_ANONYMOUS_PATH',
            edit_text=self.get_config_value('FTP_ANONYMOUS_PATH'),
            align='left', callback=self.callback)
        self.anonymous_button = FocusAttrWrap(
            urwid.Button("  Press to select folder",
                         on_press=self.callback, user_data='anonymous_button'),
            'button_content', focus_attr='button_focus')

        # address and port
        self.address = NamedEdit(
            'Address : ', name='FTP_ADDRESS',
            align='left', callback=self.callback,
            edit_text=self.get_config_value('FTP_ADDRESS'))
        self.port = NamedEdit(
            'Port : ', name='FTP_PORT',
            align='left', callback=self.callback,
            edit_text=self.get_config_value('FTP_PORT'))
        self.passive_port = NamedEdit(
            'Passive port (range 60000, 65535): ', name='FTP_PASSIVE_PORT',
            align='left', callback=self.callback,
            edit_text=self.get_config_value('FTP_PASSIVE_PORT'))

        # max connection
        self.max_connection = NamedEdit(
            'Max Connection : ', name='FTP_MAX_CONNECTION',
            align='left', callback=self.callback,
            edit_text=self.get_config_value('FTP_MAX_CONNECTION'))
        self.max_connection_per_ip = NamedEdit(
            'Max Connection Per IP : ', name='FTP_MAX_CON_PER_IP',
            align='left', callback=self.callback,
            edit_text=self.get_config_value('FTP_MAX_CON_PER_IP'))

        # banner
        self.banner = NamedEdit(
            'Welcome Banner >', name='FTP_WELCOME_BANNER',
            align='left', callback=self.callback,
            edit_text=self.get_config_value('FTP_WELCOME_BANNER'))

        self.contents = BaseTextUI.draw_title('FTP') + \
            [self.enable_root, self.root_path, self.root_button, SPLITTER,
             self.enable_anonymous, self.anonymous_path, self.anonymous_button, SPLITTER,
             self.passive_port, self.address, self.port, SPLITTER,
             self.max_connection, self.max_connection_per_ip, LINE_SPLITTER, SPLITTER,
             self.banner]
        return self.contents

    def callback(self, widget, data):
        super().save_config_data(widget, data)

        if data == 'admin_button':
            self.root_path.set_edit_text(DirectoryBrowser().show())
            self.clear_screen()
        if data == 'anonymous_button':
            self.anonymous_path.set_edit_text(DirectoryBrowser().show())
            self.clear_screen()
