from os import path
from typing import Callable

import pytest

TESTFILES_DIR = path.join(path.dirname(path.realpath(__file__)), "../testfiles")


@pytest.fixture()
def testfile() -> Callable[[str], str]:
    """Factory function for easy access to testfiles"""

    def _testfile(fn: str) -> str:
        return path.join(TESTFILES_DIR, fn)

    return _testfile


@pytest.fixture()
def testfiles_empty(testfile) -> list[str]:
    return [
        testfile("empty/empty.flac"),
        testfile("empty/empty.mp3"),
        testfile("empty/empty.wav"),
    ]


@pytest.fixture()
def testfiles_notags(testfile) -> list[str]:
    return [
        testfile("notags/notags.flac"),
        testfile("notags/notags.mp3"),
        testfile("notags/notags.wav"),
    ]


@pytest.fixture()
def testfiles_id3v1(testfile) -> list[str]:
    return [
        testfile("id3v1/id3v1.mp3"),
        testfile("id3v1/id3v1.wav"),
    ]


@pytest.fixture()
def testfiles_id3v2(testfile) -> list[str]:
    return [
        testfile("id3v2/id3v2.mp3"),
        testfile("id3v2/id3v2.wav"),  # idv2 tags in wav-files are not supported
    ]


@pytest.fixture()
def testfiles_vorbis(testfile) -> list[str]:
    return [
        testfile("vorbis/vorbis.flac"),
    ]


@pytest.fixture()
def testfiles_symlink(testfile) -> list[str]:
    return [
        testfile("symlink/id3v1.wav"),
        testfile("symlink/id3v2.wav"),
        testfile("symlink/id3v1.mp3"),
        testfile("symlink/id3v2.mp3"),
        testfile("symlink/vorbis.flac"),
        testfile("symlink/id3v1"),
        testfile("symlink/id3v2"),
        testfile("symlink/vorbis"),
    ]


@pytest.fixture()
def testfiles_perm(testfile) -> list[str]:
    return [
        testfile("perm/0x000.flac"),
        testfile("perm/0x110.flac"),
        testfile("perm/0x220.flac"),
        testfile("perm/0x440.flac"),
        testfile("perm/0x000.mp3"),
        testfile("perm/0x110.mp3"),
        testfile("perm/0x220.mp3"),
        testfile("perm/0x440.mp3"),
        testfile("perm/0x000.wav"),
        testfile("perm/0x110.wav"),
        testfile("perm/0x220.wav"),
        testfile("perm/0x440.wav"),
    ]


@pytest.fixture()
def testfiles_ext(testfile) -> list[str]:
    return [
        testfile("ext/0x000.flac"),
        testfile("ext/0x110.flac"),
        testfile("ext/0x220.flac"),
        testfile("ext/0x440.flac"),
        testfile("ext/0x000.mp3"),
        testfile("ext/0x110.mp3"),
        testfile("ext/0x220.mp3"),
        testfile("ext/0x440.mp3"),
        testfile("ext/0x000.wav"),
        testfile("ext/0x110.wav"),
        testfile("ext/0x220.wav"),
        testfile("ext/0x440.wav"),
    ]


@pytest.fixture()
def testfiles_corrupt(testfile) -> list[str]:
    return [
        # flac files
        testfile("corrupt/mp3v1_header.flac"),
        testfile("corrupt/mp3v2_header.flac"),
        testfile("corrupt/wav_header.flac"),
        # mp3 files
        testfile("corrupt/flac_header.mp3"),
        testfile("corrupt/wav_header.mp3"),
        # wav files
        testfile("corrupt/flac_header.wav"),
        testfile("corrupt/mp3v1_header.wav"),
        testfile("corrupt/mp3v2_header.wav"),
    ]
