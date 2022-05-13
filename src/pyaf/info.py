from typing import Union

from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.wave import WAVE


class Info:
    def __init__(self, obj: Union[FLAC, MP3, WAVE]) -> None:
        self._mutobj = obj

    def __repr__(self) -> str:
        return f"Info({type(self._mutobj).__name__}('{self._mutobj.filename}'))"

    @property
    def bitrate(self) -> int:
        return self._mutobj.info.bitrate  # type: ignore

    @property
    def bits_per_sample(self) -> int:
        return self._mutobj.info.bits_per_sample  # type: ignore

    @property
    def channels(self) -> int:
        return self._mutobj.info.channels  # type: ignore

    @property
    def filename(self) -> str:
        return self._mutobj.filename  # type: ignore

    @property
    def length(self) -> float:
        return self._mutobj.info.length  # type: ignore

    @property
    def mimetype(self) -> str:
        return self._mutobj.mime[0]

    @property
    def sample_rate(self) -> int:
        return self._mutobj.info.sample_rate  # type: ignore

    def as_dict(self) -> dict:
        return {
            "bitrate": self.bitrate,
            "bits_per_sample": self.bits_per_sample,
            "channels": self.channels,
            "filename": self.filename,
            "length": self.length,
            "mimetype": self.mimetype,
            "sample_rate": self.sample_rate,
        }
