from mutagen.mp3 import MP3

from pyaf.id3 import Id3


def test_Id3__init(testfile):
    assert isinstance(Id3(MP3(testfile("id3v2/id3v2.mp3"))), Id3)


def test_Id3__attrs():
    assert hasattr(Id3, "save")
    assert hasattr(Id3, "wipe")
    assert hasattr(Id3, "album")
    assert hasattr(Id3, "albumartist")
    assert hasattr(Id3, "title")
    assert hasattr(Id3, "tracknumber")
    assert hasattr(Id3, "totaltracks")
    assert hasattr(Id3, "discnumber")
    assert hasattr(Id3, "totaldiscs")


def test_Id3__Id3Core_getter_album(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.album == "test_album"


def test_Id3__Id3Core_getter_albumartist(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.albumartist == "test_albumartist"


def test_Id3__Id3Core_getter_title(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.title == "test_title"


def test_Id3__Id3Core_getter_tracknumber(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.tracknumber == 1


def test_Id3__Id3Core_getter_totaltracks(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.totaltracks == 1


def test_Id3__Id3Core_getter_discnumber(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.discnumber == 1


def test_Id3__Id3Core_getter_totaldiscs(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.totaldiscs == 1
