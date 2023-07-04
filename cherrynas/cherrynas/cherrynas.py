import pynecone as pc

from cherrynas.state import State

from cherrynas.pages.index import index
from cherrynas.pages.music import music_index
from cherrynas.pages.music import music_scripts

app = pc.App(state=State)
app.add_page(index, title="cherrynas", image="/splash.png")
app.add_page(music_index, title="cherrynas ❤ music", route="/music", script_tags=[music_scripts()])
app.compile()