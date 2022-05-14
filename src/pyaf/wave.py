from mutagen.wave import WAVE

from pyaf.id3 import Id3
from pyaf.info import Info


class Wave:
    def __init__(self, fn: str) -> None:
        self._mutobj = WAVE(fn)
        self.info = Info(self._mutobj)
        self.tags = Id3(self._mutobj)
