from mutagen.wave import WAVE


class Wave:
    def __init__(self, fn: str) -> None:
        self._mutobj = WAVE(fn)
