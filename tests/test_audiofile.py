import pytest

from pyaf.audiofile import (
    Audiofile,
    Audiofile_T,
)
from pyaf.flac import Flac
from pyaf.mp3 import Mp3
from pyaf.wave import Wave


def test_Audiofile__init_flac_file(testfile):
    af = Audiofile(testfile("notags/notags.flac"))
    assert isinstance(af, Audiofile_T)
    assert isinstance(af, Flac)


def test_Audiofile__init_mp3_file(testfile):
    af = Audiofile(testfile("notags/notags.mp3"))
    assert isinstance(af, Audiofile_T)
    assert isinstance(af, Mp3)


def test_Audiofile__init_wav_file(testfile):
    af = Audiofile(testfile("notags/notags.wav"))
    assert isinstance(af, Audiofile_T)
    assert isinstance(af, Wave)


def test_Audiofile__init_empty_string():
    with pytest.raises(ValueError):
        Audiofile("")


def test_Audiofile__init_noexists_file():
    with pytest.raises(FileNotFoundError):  # FileNotFoundError is equal to OSError
        Audiofile("non_exists.wav")


def test_Audiofile__init_empty_file(testfile):
    with pytest.raises(ValueError):
        Audiofile(testfile("empty/empty.flac"))


def test_Audiofile__init_skrew_extension_on_valid_audiofile(testfile):
    with pytest.raises(ValueError):
        Audiofile(testfile("ext/wrong_ext.flac.mp3"))

    with pytest.raises(ValueError):
        Audiofile(testfile("ext/wrong_ext.flac.wav"))

    with pytest.raises(ValueError):
        Audiofile(testfile("ext/wrong_ext.mp3.flac"))

    with pytest.raises(ValueError):
        Audiofile(testfile("ext/wrong_ext.mp3.wav"))

    with pytest.raises(ValueError):
        Audiofile(testfile("ext/wrong_ext.wav.flac"))

    with pytest.raises(ValueError):
        Audiofile(testfile("ext/wrong_ext.wav.mp3"))


def test_Audiofile__init_wrong_extension_on_valid_audiofile(testfile):
    with pytest.raises(ValueError):
        Audiofile(testfile("ext/wrong_ext.flac.txt"))

    with pytest.raises(ValueError):
        Audiofile(testfile("ext/wrong_ext.mp3.txt"))

    with pytest.raises(ValueError):
        Audiofile(testfile("ext/wrong_ext.wav.txt"))


# def test_Audiofile__init_wrong_extension_on_ascii_file(testfile):  # TODO
#     pass


def test_Audiofile__init_symlink(testfile):
    af = Audiofile(testfile("symlink/vorbis.flac"))
    assert isinstance(af, Audiofile_T)
    assert isinstance(af, Flac)

    af = Audiofile(testfile("symlink/id3v2.mp3"))
    assert isinstance(af, Audiofile_T)
    assert isinstance(af, Mp3)

    af = Audiofile(testfile("symlink/id3v1.wav"))
    assert isinstance(af, Audiofile_T)
    assert isinstance(af, Wave)


def test_Audiofile__init_permission_0x000(testfile):
    with pytest.raises(PermissionError):  # is equal to OSError w/ errno == 3
        Audiofile(testfile("perm/0x000.mp3"))


def test_Audiofile__init_permission_0x110(testfile):
    with pytest.raises(PermissionError):
        Audiofile(testfile("perm/0x110.mp3"))


def test_Audiofile__init_permission_0x220(testfile):
    with pytest.raises(PermissionError):
        Audiofile(testfile("perm/0x220.mp3"))


def test_Audiofile__init_permission_0x440(testfile):
    af = Audiofile(testfile("perm/0x440.mp3"))
    assert isinstance(af, Audiofile_T)
    assert isinstance(af, Mp3)


def test_Audiofile__init_flac_file_with_mp3v1_header(testfile):
    with pytest.raises(ValueError):
        Audiofile(testfile("corrupt/mp3v1_header.flac"))


def test_Audiofile__init_flac_file_with_mp3v2_header(testfile):
    with pytest.raises(ValueError):
        Audiofile(testfile("corrupt/mp3v2_header.flac"))


def test_Audiofile__init_flac_file_with_wav_header(testfile):
    with pytest.raises(ValueError):
        Audiofile(testfile("corrupt/wav_header.flac"))


# TODO: This should fail??
# TODO: Bug report on gh??
# def test_Audiofile__init_mp3_file_with_flac_header(testfile):
#     with pytest.raises(ValueError):
#         Audiofile(testfile("corrupt/flac_header.mp3"))


# TODO: This should fail??
# TODO: Bug report on gh??
# def test_Audiofile__init_mp3_file_with_wav_header(testfile):
#     with pytest.raises(ValueError):
#         Audiofile(testfile("corrupt/wav_header.mp3"))


def test_Audiofile__init_wav_file_with_flac_header(testfile):
    with pytest.raises(ValueError):
        Audiofile(testfile("corrupt/flac_header.wav"))


def test_Audiofile__init_wav_file_with_mp3v1_header(testfile):
    with pytest.raises(ValueError):
        Audiofile(testfile("corrupt/mp3v1_header.wav"))


def test_Audiofile__init_wav_file_with_mp3v2_header(testfile):
    with pytest.raises(ValueError):
        Audiofile(testfile("corrupt/mp3v2_header.wav"))
