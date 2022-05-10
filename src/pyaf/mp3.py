from mutagen.mp3 import MP3


class Mp3:
    def __init__(self, fn: str) -> None:
        self._mutobj = MP3(fn)
