from mutagen.flac import FLAC

from pyaf.info import Info
from pyaf.vorbis import Vorbis


class Flac:
    def __init__(self, fn: str) -> None:
        self._mutobj = FLAC(fn)
        self.info = Info(self._mutobj)
        self.tags = Vorbis(self._mutobj)
