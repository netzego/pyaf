from mutagen.flac import FLAC

from pyaf.vorbis import Vorbis


def test_Vorbis__init(testfile):
    assert isinstance(Vorbis(FLAC(testfile("vorbis/vorbis.flac"))), Vorbis)


def test_Vorbis__attrs():
    assert hasattr(Vorbis, "save")
    assert hasattr(Vorbis, "wipe")
