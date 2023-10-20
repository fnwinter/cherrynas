import reflex as rx

from cherrynas.state import State
from cherrynas.pages.music.music_tag import parse_audio_tag

def music_scripts():
    _html = '''<script src='/javascripts/music.js'></script>'''
    return rx.html(_html)

def grid_item(_text, _width, _align, _span):
    return rx.grid_item(rx.box(rx.text(_text), width=_width), row_span=1, col_span=_span)

def album_cover():
    return rx.image(src="/images/album_art.png", width="200px", height="200px", border_radius="lg")

def album_info():
    song = parse_audio_tag('../../../assets/temp/02_Song 2.mp3')
    print(song)

    return rx.grid(
        grid_item("🎶", '10px', 'right',1),
        grid_item(song['title'], '100%', 'left',3),
        grid_item("💽", '10px','right',1),
        grid_item("beetlebum",'100%', 'left',3),
        grid_item("🧑", '10px','right',1),
        grid_item("blur", '100%','left',3),
        grid_item("🎷", '10px','right',1),
        grid_item("rock", '100%','left',3),
        template_rows="repeat(4, 1fr)",
        template_columns="repeat(4, 1fr)",
        hieght="200px",
        width="100%",
        gap=0)

def media_player():
    # https://www.w3schools.com/tags/ref_av_dom.asp
    return rx.html("<audio id='audio_player'><source src='horse.ogg' type='audio/ogg'></audio>")

def music_controller():
    return rx.button_group(
        rx.button("◀◀", bg="#909090", color="#323232", size="sm"),
        rx.button("▶", bg="#909090", color="#323232", size="sm"),
        rx.button("■", bg="#909090", color="#323232", size="sm"),
        rx.button("▶▶", bg="#909090", color="#323232", size="sm"),
        rx.button("⫶", bg="#909090", color="#323232", size="sm", on_click=PlayerList.right),
        space="1em")

class PlayerList(State):
    show_right: bool = False
    show_top: bool = False

    def top(self):
        self.show_top = not (self.show_top)

    def right(self):
        self.show_right = not (self.show_right)

def music_playlist():
    return rx.box(
            rx.drawer(
                rx.drawer_overlay(
                    rx.drawer_content(
                        rx.drawer_header("Playlist"),
                        rx.drawer_body(
                            "Song2"
                        ),
                        rx.drawer_footer(
                            rx.button(
                                "+", on_click=PlayerList.right
                            ),
                            rx.button(
                                "-", on_click=PlayerList.right
                            ),
                            rx.button(
                                "Clear", on_click=PlayerList.right
                            ),
                            rx.button(
                                "X", on_click=PlayerList.right
                            )
                        ),
                        bg="white",
                    )
                ),
                is_open=PlayerList.show_right,
            ),
        )

def music_index():
    return rx.center(
        rx.vstack(
            album_cover(),
            album_info(),
            media_player(),
            music_controller(),
            music_playlist(),
            bg="#E3E3E3",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
    )