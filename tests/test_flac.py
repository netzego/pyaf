import pytest
from mutagen import MutagenError
from mutagen.flac import (
    FLAC,
    FLACNoHeaderError,
)

from pyaf.flac import Flac


def test_Flac__init(testfile):
    af = Flac(testfile("notags/notags.flac"))
    assert isinstance(af, Flac)


def test_Flac__class_attr(testfile):
    af = Flac(testfile("notags/notags.flac"))
    assert hasattr(af, "_mutobj")
    assert isinstance(af._mutobj, FLAC)


def test_Flac__init_empty_string():
    with pytest.raises(MutagenError):
        Flac("")


def test_Flac__init_non_existing_filename():
    with pytest.raises(MutagenError):
        Flac("non_exists.flac")


def test_Flac__init_empty_file(testfile):
    with pytest.raises(MutagenError):
        Flac(testfile("empty/empty.flac"))


def test_Flac__init_wrong_filetype_mp3(testfile):
    with pytest.raises(MutagenError):
        Flac(testfile("notags/notags.mp3"))


def test_Flac__init_wrong_filetype_wav(testfile):
    with pytest.raises(MutagenError):
        Flac(testfile("notags/notags.wav"))


def test_Flac__init_flac_with_mp3_extension(testfile):
    af = Flac(testfile("ext/wrong_ext.flac.mp3"))
    assert isinstance(af, Flac)  # This works!


def test_Flac__init_mp3_with_flac_extension(testfile):
    with pytest.raises(FLACNoHeaderError):
        Flac(testfile("ext/wrong_ext.mp3.flac"))


def test_Flac__init_corrupt_flac_with_mp3v1_header(testfile):
    with pytest.raises(FLACNoHeaderError):
        Flac(testfile("corrupt/mp3v1_header.flac"))


def test_Flac__init_corrupt_flac_with_mp3v2_header(testfile):
    with pytest.raises(FLACNoHeaderError):
        Flac(testfile("corrupt/mp3v2_header.flac"))


def test_Flac__init_corrupt_flac_with_wav_header(testfile):
    with pytest.raises(FLACNoHeaderError):
        Flac(testfile("corrupt/wav_header.flac"))
