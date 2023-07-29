import eyed3
import os

from eyed3.id3.frames import ImageFrame
from collections import defaultdict

eyed3.log.setLevel("ERROR")

def write_album_art(images):
    if len(images) == 1:
        with open("album_art.png","wb") as f:
            f.write(images[0])
            return

    for af in images:
        if af.picture_type == ImageFrame.FRONT_COVER:
            with open("album_art.png","wb") as f:
                f.write(af.image_data)
                return

    image = images[-1]
    with open("album_art.png","wb") as f:
        f.write(image.image_data)

def parse_audio_tag(path):
    if os.path.exists(path):
        audiofile = eyed3.load(path)
        if audiofile:
            write_album_art(audiofile.tag.images)
            return {'title': audiofile.tag.title,
                    'album': audiofile.tag.album,
                    'artist': audiofile.tag.artist,
                    'genre': audiofile.tag.genre}
    return defaultdict(str)