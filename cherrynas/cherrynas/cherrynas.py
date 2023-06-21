"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc

from cherrynas.pages.music import music_index
from pcconfig import config

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

class State(pc.State):
    """The app state."""
    print("pass")

def index():
    return pc.text("hello world")

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(music_index, route="/music")
app.compile()
