from mutagen.mp3 import MP3

from pyaf.id3v2 import Id3v2


def test_Id3v2__init(testfile):
    assert isinstance(Id3v2(MP3(testfile("id3v2/id3v2.mp3"))), Id3v2)


def test_Id3v2__attrs():
    assert hasattr(Id3v2, "save")
    assert hasattr(Id3v2, "wipe")
