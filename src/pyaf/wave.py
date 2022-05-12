from mutagen.wave import WAVE

from pyaf.info import Info


class Wave:
    def __init__(self, fn: str) -> None:
        self._mutobj = WAVE(fn)
        self.info = Info(self._mutobj)
