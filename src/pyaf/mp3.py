from mutagen.mp3 import MP3

from pyaf.id3v2 import Id3v2
from pyaf.info import Info


class Mp3:
    def __init__(self, fn: str) -> None:
        self._mutobj = MP3(fn)
        self.info = Info(self._mutobj)
        self.tags = Id3v2(self._mutobj)
