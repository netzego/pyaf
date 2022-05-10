from mutagen.flac import FLAC


class Flac:
    def __init__(self, fn: str) -> None:
        self._mutobj = FLAC(fn)
