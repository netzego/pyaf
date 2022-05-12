import errno
from typing import Union

from mutagen import MutagenError
from mutagen._iff import (
    EmptyChunk,
    InvalidChunk,
)
from mutagen.flac import FLACNoHeaderError as FlacHeaderError
from mutagen.flac import error as FlacError
from mutagen.mp3 import HeaderNotFoundError as Mp3HeaderError
from mutagen.wave import error as WaveError

from pyaf.flac import Flac
from pyaf.mp3 import Mp3
from pyaf.wave import Wave

Audiofile_T = Union[Flac, Mp3, Wave]


def Audiofile(fn: str) -> Audiofile_T:
    """A factory function for `Flac`, `Mp3` and `Wave` class which unifies error msgs"""
    try:
        if fn.lower().endswith("flac"):
            return Flac(fn)

        elif fn.lower().endswith("mp3"):
            return Mp3(fn)

        elif fn.lower().endswith("wav"):
            return Wave(fn)

        raise NotImplementedError

    except Exception as e:
        if isinstance(e, NotImplementedError):
            raise ValueError(f"`{fn}': Unsupported filetype.")

        if isinstance(
            e,
            (
                EmptyChunk,
                FlacError,
                FlacHeaderError,
                InvalidChunk,
                Mp3HeaderError,
                WaveError,
            ),
        ):
            raise ValueError(f"`{fn}': IO error.")
            # raise MutagenError(f"`{fn}': IO error.")

        if isinstance(e, MutagenError):
            _errno = e.args[0].errno

            if _errno == errno.ENOENT:
                raise OSError(_errno, f"`{fn}': File or directory not found.")

            if _errno == errno.EACCES:
                raise OSError(_errno, f"`{fn}': Could not read file or directory.")

        raise NotImplementedError("This should not happen")
