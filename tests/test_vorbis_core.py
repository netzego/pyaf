from pyaf.vorbis_core import VorbisCore


def test_VorbisCore__init():
    assert isinstance(VorbisCore(), VorbisCore)


def test_VorbisCore__attrs():
    assert hasattr(VorbisCore, "album")
    assert hasattr(VorbisCore, "albumartist")
    assert hasattr(VorbisCore, "artist")
    assert hasattr(VorbisCore, "title")
    assert hasattr(VorbisCore, "tracknumber")
    assert hasattr(VorbisCore, "totaltracks")
    assert hasattr(VorbisCore, "discnumber")
    assert hasattr(VorbisCore, "totaldiscs")
