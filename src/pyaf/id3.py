from typing import Union

from mutagen.mp3 import MP3
from mutagen.wave import WAVE

from pyaf.id3_core import Id3Core


class Id3(Id3Core):
    def __init__(self, mutobj: Union[MP3, WAVE]) -> None:
        self._mutobj = mutobj

    def __repr__(self) -> str:
        return f"Id3({type(self._mutobj).__name__}('{self._mutobj.filename}'))"

    def save(self) -> None:
        raise NotImplementedError

    def wipe(self) -> None:
        raise NotImplementedError