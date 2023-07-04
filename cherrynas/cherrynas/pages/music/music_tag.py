import eyed3

from eyed3.id3.frames import ImageFrame

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
    audiofile = eyed3.load('../../../assets/temp/02_Song 2.mp3')

    write_album_art(audiofile.tag.images)

    return {'title': audiofile.tag.title, 'album': audiofile.tag.album, 'artist': audiofile.tag.artist, 'genre': audiofile.tag.genre}
