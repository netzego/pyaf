from mutagen.mp3 import MP3

from pyaf.id3v2 import Id3v2


def test_Id3v2__init(testfile):
    assert isinstance(Id3v2(MP3(testfile("id3v2/id3v2.mp3"))), Id3v2)


def test_Id3v2__attrs():
    assert hasattr(Id3v2, "save")
    assert hasattr(Id3v2, "wipe")
    assert hasattr(Id3v2, "album")
    assert hasattr(Id3v2, "albumartist")
    assert hasattr(Id3v2, "title")
    assert hasattr(Id3v2, "tracknumber")
    assert hasattr(Id3v2, "totaltracks")
    assert hasattr(Id3v2, "discnumber")
    assert hasattr(Id3v2, "totaldiscs")


def test_Id3v2__Id3v2Core_getter_album(testfile):
    mp3 = Id3v2(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.album == "test_album"


def test_Id3v2__Id3v2Core_getter_albumartist(testfile):
    mp3 = Id3v2(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.albumartist == "test_albumartist"


def test_Id3v2__Id3v2Core_getter_title(testfile):
    mp3 = Id3v2(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.title == "test_title"


def test_Id3v2__Id3v2Core_getter_tracknumber(testfile):
    mp3 = Id3v2(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.tracknumber == 1


def test_Id3v2__Id3v2Core_getter_totaltracks(testfile):
    mp3 = Id3v2(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.totaltracks == 1


def test_Id3v2__Id3v2Core_getter_discnumber(testfile):
    mp3 = Id3v2(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.discnumber == 1


def test_Id3v2__Id3v2Core_getter_totaldiscs(testfile):
    mp3 = Id3v2(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.totaldiscs == 1
