import pytest
from mutagen import MutagenError
from mutagen._iff import (
    EmptyChunk,
    InvalidChunk,
)
from mutagen.wave import WAVE

from pyaf.wave import Wave


def test_Wave__init(testfile):
    af = Wave(testfile("notags/notags.wav"))
    assert isinstance(af, Wave)


def test_Wave__class_attr(testfile):
    af = Wave(testfile("notags/notags.wav"))
    assert hasattr(af, "_mutobj")
    assert isinstance(af._mutobj, WAVE)


def test_Wave__init_empty_string():
    with pytest.raises(MutagenError):
        Wave("")


def test_Wave__init_non_existing_filename():
    with pytest.raises(MutagenError):
        Wave("non_exists.wav")


def test_Wave__init_empty_file(testfile):
    with pytest.raises(MutagenError):
        Wave(testfile("empty/empty.wav"))


def test_Wave__init_wrong_filetype_flac(testfile):
    with pytest.raises(MutagenError):
        Wave(testfile("notags/notags.flac"))


def test_Wave__init_wrong_filetype_mp3(testfile):
    with pytest.raises(MutagenError):
        Wave(testfile("notags/notags.mp3"))


def test_Wave__init_wav_with_mp3_extension(testfile):
    af = Wave(testfile("ext/wrong_ext.wav.mp3"))
    assert isinstance(af, Wave)  # This works!


def test_Wave__init_mp3_with_wav_extension(testfile):
    with pytest.raises(InvalidChunk):
        Wave(testfile("ext/wrong_ext.mp3.wav"))


def test_Wave__init_corrupt_wav_with_flac_header(testfile):
    with pytest.raises(InvalidChunk):
        Wave(testfile("corrupt/flac_header.wav"))


def test_Wave__init_corrupt_wav_with_mp3v1_header(testfile):
    with pytest.raises(InvalidChunk):
        Wave(testfile("corrupt/mp3v1_header.wav"))


def test_Wave__init_corrupt_wav_with_mp3v2_header(testfile):
    with pytest.raises(InvalidChunk):
        Wave(testfile("corrupt/mp3v2_header.wav"))
