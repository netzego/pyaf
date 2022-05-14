from mutagen.flac import FLAC

from pyaf.vorbis_core import VorbisCore


class Vorbis(VorbisCore):
    def __init__(self, mutobj: FLAC) -> None:
        self._mutobj = mutobj

    def __repr__(self) -> str:
        return f"Vorbis({type(self._mutobj).__name__}('{self._mutobj.filename}'))"

    def save(self) -> None:
        raise NotImplementedError

    def wipe(self) -> None:
        raise NotImplementedError

    @property
    def version(self) -> tuple[int]:
        return self._mutobj.tags.version  # type: ignore
