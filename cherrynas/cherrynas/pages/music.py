# music page
import pynecone as pc

from typing import List

options: List[str] = ["Title", "Artist", "Album", "Genre"]

class SelectState(pc.State):
    option: str = "Search by"

class InputState(pc.State):
    text: str = "Search"

def grid_item(_text):
    return pc.grid_item(
        pc.center(pc.text(_text)),
        row_span=1, col_span=1)

def media_player():
    # https://www.w3schools.com/tags/ref_av_dom.asp
    return pc.html("<audio controls><source src='horse.ogg' type='audio/ogg'></audio>")

def music_index():
    return pc.center(
        pc.vstack(
            pc.html("<script scr='/javascripts/music_page.js'></script>"),
            pc.hstack(
                        pc.select(
                        options,
                        placeholder="Select by",
                        on_change=SelectState.set_option,
                        color_schemes="twitter",
                    ),
                pc.input(on_change=InputState.set_text),
            ),
            pc.image(src="/images/album_art.png", width="200px", height="200px"),
            pc.grid(
                grid_item("title"),
                grid_item("song 2"),
                grid_item("album"),
                grid_item("beetlebum"),
                grid_item("artist"),
                grid_item("blur"),
                grid_item("genre"),
                grid_item("rock"),
                template_rows="repeat(4, 1fr)",
                template_columns="repeat(2, 1fr)",
                hieght="200px",
                width="100%",
                gap=0,
            ),
            media_player(),
            pc.button_group(
                pc.button(
                    "Prev", bg="lightblue", color="black", size="sm"
                ),
                pc.button(
                    "Play", bg="orange", color="white", size="sm"
                ),
                pc.button("Next", color_scheme="red", size="sm"),
                space="1em",
            ),
            bg="white",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
    )
