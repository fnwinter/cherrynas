"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

from cherrynas.state import State

from cherrynas.pages.index import index
from cherrynas.pages.music.music_page import music_index
from cherrynas.pages.music.music_page import music_scripts

app = rx.App(state=State)
app.add_page(index, title="cherrynas", image="/splash.png")
app.add_page(music_index, title="cherrynas ❤ music", route="/music", script_tags=[music_scripts()])
app.compile()