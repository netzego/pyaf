from pyaf.id3v2_core import Id3v2Core


def test_Id3v2Core__init():
    assert isinstance(Id3v2Core(), Id3v2Core)


def test_Id3v2Core__attrs():
    assert hasattr(Id3v2Core, "album")
    assert hasattr(Id3v2Core, "albumartist")
    assert hasattr(Id3v2Core, "artist")
    assert hasattr(Id3v2Core, "title")
    assert hasattr(Id3v2Core, "tracknumber")
    assert hasattr(Id3v2Core, "totaltracks")
    assert hasattr(Id3v2Core, "discnumber")
    assert hasattr(Id3v2Core, "totaldiscs")
