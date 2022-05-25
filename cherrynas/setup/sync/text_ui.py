# Copyright 2019 fnwinter@gmail.com

from gui.base_text_ui import BaseTextUI

class TextUI(BaseTextUI):
    """
    Text UI for Sync
    """
    def __init__(self):
        super().__init__('SYNC')

    @staticmethod
    def get_label():
        return "Sync"

    def draw_text_ui(self):
        return BaseTextUI.draw_title("Sync folders")
