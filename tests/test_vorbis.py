from mutagen.flac import FLAC

from pyaf.vorbis import Vorbis


def test_Vorbis__init(testfile):
    assert isinstance(Vorbis(FLAC(testfile("vorbis/vorbis.flac"))), Vorbis)


def test_Vorbis__attrs():
    assert hasattr(Vorbis, "save")
    assert hasattr(Vorbis, "wipe")
    assert hasattr(Vorbis, "album")
    assert hasattr(Vorbis, "albumartist")
    assert hasattr(Vorbis, "title")
    assert hasattr(Vorbis, "tracknumber")
    assert hasattr(Vorbis, "totaltracks")
    assert hasattr(Vorbis, "discnumber")
    assert hasattr(Vorbis, "totaldiscs")


def test_Vorbis__VorbisCore_getter_album_notags(testfile):
    vorbis = Vorbis(FLAC(testfile("notags/notags.flac")))
    assert vorbis.album == None


def test_Vorbis__VorbisCore_getter_album(testfile):
    vorbis = Vorbis(FLAC(testfile("vorbis/vorbis.flac")))
    assert vorbis.album == "test_album"


def test_Vorbis__VorbisCore_getter_albumartist_notags(testfile):
    vorbis = Vorbis(FLAC(testfile("notags/notags.flac")))
    assert vorbis.albumartist == None


def test_Vorbis__VorbisCore_getter_albumartist(testfile):
    vorbis = Vorbis(FLAC(testfile("vorbis/vorbis.flac")))
    assert vorbis.albumartist == "test_albumartist"


def test_Vorbis__VorbisCore_getter_artist_notags(testfile):
    vorbis = Vorbis(FLAC(testfile("notags/notags.flac")))
    assert vorbis.artist == None


def test_Vorbis__VorbisCore_getter_artist(testfile):
    vorbis = Vorbis(FLAC(testfile("vorbis/vorbis.flac")))
    assert vorbis.artist == "test_artist"


def test_Vorbis__VorbisCore_getter_title_notags(testfile):
    vorbis = Vorbis(FLAC(testfile("notags/notags.flac")))
    assert vorbis.title == None


def test_Vorbis__VorbisCore_getter_title(testfile):
    vorbis = Vorbis(FLAC(testfile("vorbis/vorbis.flac")))
    assert vorbis.title == "test_title"


def test_Vorbis__VorbisCore_getter_tracknumber_notags(testfile):
    vorbis = Vorbis(FLAC(testfile("notags/notags.flac")))
    assert vorbis.tracknumber == None


def test_Vorbis__VorbisCore_getter_tracknumber(testfile):
    vorbis = Vorbis(FLAC(testfile("vorbis/vorbis.flac")))
    assert vorbis.tracknumber == 1


def test_Vorbis__VorbisCore_getter_totaltracks_notags(testfile):
    vorbis = Vorbis(FLAC(testfile("notags/notags.flac")))
    assert vorbis.totaltracks == None


def test_Vorbis__VorbisCore_getter_totaltracks(testfile):
    vorbis = Vorbis(FLAC(testfile("vorbis/vorbis.flac")))
    assert vorbis.totaltracks == 1


def test_Vorbis__VorbisCore_getter_discnumber_notags(testfile):
    vorbis = Vorbis(FLAC(testfile("notags/notags.flac")))
    assert vorbis.discnumber == None


def test_Vorbis__VorbisCore_getter_discnumber(testfile):
    vorbis = Vorbis(FLAC(testfile("vorbis/vorbis.flac")))
    assert vorbis.discnumber == 1


def test_Vorbis__VorbisCore_getter_totaldiscs_notags(testfile):
    vorbis = Vorbis(FLAC(testfile("notags/notags.flac")))
    assert vorbis.totaldiscs == None


def test_Vorbis__VorbisCore_getter_totaldiscs(testfile):
    vorbis = Vorbis(FLAC(testfile("vorbis/vorbis.flac")))
    assert vorbis.totaldiscs == 1
