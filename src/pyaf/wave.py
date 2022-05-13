from mutagen.wave import WAVE

from pyaf.id3v2 import Id3v2
from pyaf.info import Info


class Wave:
    def __init__(self, fn: str) -> None:
        self._mutobj = WAVE(fn)
        self.info = Info(self._mutobj)
        self.tags = Id3v2(self._mutobj)
