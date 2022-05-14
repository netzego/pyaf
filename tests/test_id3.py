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


def test_Id3__Id3Core_getter_album_notags(testfile):
    mp3 = Id3(MP3(testfile("notags/notags.mp3")))
    assert mp3.album == None


def test_Id3__Id3Core_getter_album_id3v2_mp3(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.album == "test_album"


def test_Id3__Id3Core_getter_albumartist_notags(testfile):
    mp3 = Id3(MP3(testfile("notags/notags.mp3")))
    assert mp3.albumartist == None


def test_Id3__Id3Core_getter_albumartist_id3v2_mp3(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.albumartist == "test_albumartist"


def test_Id3__Id3Core_getter_title_notags(testfile):
    mp3 = Id3(MP3(testfile("notags/notags.mp3")))
    assert mp3.title == None


def test_Id3__Id3Core_getter_title_id3v2_mp3(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.title == "test_title"


def test_Id3__Id3Core_getter_tracknumber_notags(testfile):
    mp3 = Id3(MP3(testfile("notags/notags.mp3")))
    assert mp3.tracknumber == None


def test_Id3__Id3Core_getter_tracknumber_id3v2_mp3(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.tracknumber == 1


def test_Id3__Id3Core_getter_totaltracks_notags(testfile):
    mp3 = Id3(MP3(testfile("notags/notags.mp3")))
    assert mp3.totaltracks == None


def test_Id3__Id3Core_getter_totaltracks_id3v2_mp3(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.totaltracks == 1


def test_Id3__Id3Core_getter_discnumber_notags(testfile):
    mp3 = Id3(MP3(testfile("notags/notags.mp3")))
    assert mp3.discnumber == None


def test_Id3__Id3Core_getter_discnumber_id3v2_mp3(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.discnumber == 1


def test_Id3__Id3Core_getter_totaldiscs_notags(testfile):
    mp3 = Id3(MP3(testfile("notags/notags.mp3")))
    assert mp3.totaldiscs == None


def test_Id3__Id3Core_getter_totaldiscs_id3v2_mp3(testfile):
    mp3 = Id3(MP3(testfile("id3v2/id3v2.mp3")))
    assert mp3.totaldiscs == 1
