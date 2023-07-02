import pynecone as pc

from cherrynas.pages.music import music_index
from cherrynas.pages.music import music_scripts

class State(pc.State):
    """The app state."""
    print("pass")

def index():
    return pc.text("hello world")

app = pc.App(state=State)
app.add_page(index, title="cherrynas", image="/splash.png")
app.add_page(music_index, title="cherrynas ❤ music", route="/music", script_tags=[music_scripts()])
app.compile()