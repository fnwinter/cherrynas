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

from base.gui.widget import SPLITTER
from base.utils.email import valid_email
from base.utils.hash import hashed_password
from modules.base_text_ui import BaseTextUI

class TextUI(BaseTextUI):
    """
    Text UI for Account
    """
    def __init__(self):
        super().__init__('ACCOUNT')
        self.email = urwid.Edit(u"      ID (Email) : ", align='left')
        self.password1 = urwid.Edit(u"        Password : ", align='left', mask=u"*")
        self.password2 = urwid.Edit(u"Confirm Password : ", align='left', mask=u"*")
        self.notice = urwid.Text(u"", align='left')

    @staticmethod
    def get_label():
        return u"Account"

    def draw_text_ui(self):
        self.email.set_edit_text(self.config_data.get('ACCOUNT_EMAIL'))
        desc = urwid.Text(u"# You can create an user account in web ui.", align='left')

        urwid.connect_signal(self.email, 'change', self.edit_email_changed)
        urwid.connect_signal(self.password1, 'change', self.edit_password_changed)
        urwid.connect_signal(self.password2, 'change', self.edit_password_changed)

        self.contents = BaseTextUI.draw_title(u"Administrator Account") +\
            [self.email, SPLITTER,
             self.password1, self.password2, SPLITTER,
             desc, self.notice]
        return self.contents

    def edit_email_changed(self, _, text):
        if valid_email(text):
            self.config_data['ACCOUNT_EMAIL'] = text
            self.notice.set_text('')
        else:
            self.notice.set_text('# Invalid Email format')

    def edit_password_changed(self, widget, text):
        pwd1 = text if self.password1 == widget else self.password1.get_edit_text()
        pwd2 = text if self.password2 == widget else self.password2.get_edit_text()
        if pwd1 == pwd2 and pwd1 != '':
            self.config_data['ACCOUNT_PASSWORD'] = hashed_password(pwd1)
            self.notice.set_text('')
        else:
            self.notice.set_text('# Confirm password is different')
