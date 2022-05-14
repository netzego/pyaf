from pyaf.id3_core import Id3Core


def test_Id3Core__init():
    assert isinstance(Id3Core(), Id3Core)


def test_Id3Core__attrs():
    assert hasattr(Id3Core, "album")
    assert hasattr(Id3Core, "albumartist")
    assert hasattr(Id3Core, "artist")
    assert hasattr(Id3Core, "title")
    assert hasattr(Id3Core, "tracknumber")
    assert hasattr(Id3Core, "totaltracks")
    assert hasattr(Id3Core, "discnumber")
    assert hasattr(Id3Core, "totaldiscs")
