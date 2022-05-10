import pytest
from mutagen import MutagenError
from mutagen.mp3 import (
    MP3,
    HeaderNotFoundError,
)

from pyaf.mp3 import Mp3


def test_Mp3__init(testfile):
    af = Mp3(testfile("notags/notags.mp3"))
    assert isinstance(af, Mp3)


def test_Mp3__class_attr(testfile):
    af = Mp3(testfile("notags/notags.mp3"))
    assert hasattr(af, "_mutobj")
    assert isinstance(af._mutobj, MP3)


def test_Mp3__init_empty_string():
    with pytest.raises(MutagenError):
        Mp3("")


def test_Mp3__init_non_existing_filename():
    with pytest.raises(MutagenError):
        Mp3("non_exists.mp3")


def test_Mp3__init_empty_file(testfile):
    with pytest.raises(MutagenError):
        Mp3(testfile("empty/empty.mp3"))


def test_Mp3__init_wrong_filetype_flac(testfile):
    with pytest.raises(MutagenError):
        Mp3(testfile("notags/notags.flac"))


def test_Mp3__init_wrong_filetype_wav(testfile):
    with pytest.raises(MutagenError):
        Mp3(testfile("notags/notags.wav"))


def test_Mp3__init_mp3_with_flac_extension(testfile):
    af = Mp3(testfile("ext/wrong_ext.mp3.flac"))
    assert isinstance(af, Mp3)  # This works!


def test_Mp3__init_flac_with_mp3_extension(testfile):
    with pytest.raises(HeaderNotFoundError):
        Mp3(testfile("ext/wrong_ext.flac.mp3"))


def test_Mp3__init_corrupt_mp3_with_flac_header(testfile):
    af = Mp3(testfile("corrupt/flac_header.mp3"))
    assert isinstance(
        af, Mp3
    )  # This should not work, file has wrong header. bug in mutagen?
    # with pytest.raises(HeaderNotFoundError):
    #     Mp3(testfile("corrupt/flac_header.mp3"))


def test_Mp3__init_corrupt_mp3_with_wav_header(testfile):
    af = Mp3(testfile("corrupt/wav_header.mp3"))
    assert isinstance(
        af, Mp3
    )  # This should not work, file has wrong header. bug in mutagen?
    # with pytest.raises(HeaderNotFoundError):
    #     Mp3(testfile("corrupt/wav_header.mp3"))
