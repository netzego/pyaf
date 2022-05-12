from typing import Callable

from mutagen.flac import FLAC

from pyaf.info import Info


def test_Info__init(testfile):
    info = Info(FLAC(testfile("vorbis/vorbis.flac")))
    assert isinstance(info, Info)


def test_Info__attr_mutobj(testfile):
    info = Info(FLAC(testfile("vorbis/vorbis.flac")))
    assert isinstance(info._mutobj, FLAC)
    assert hasattr(info, "_mutobj")


def test_Info__attrs(testfile):
    info = Info(FLAC(testfile("vorbis/vorbis.flac")))
    assert hasattr(info, "bitrate")
    assert hasattr(info, "bits_per_sample")
    assert hasattr(info, "channels")
    assert hasattr(info, "filename")
    assert hasattr(info, "length")
    assert hasattr(info, "mimetype")
    assert hasattr(info, "sample_rate")


def test_Info__methods(testfile):
    info = Info(FLAC(testfile("vorbis/vorbis.flac")))
    assert isinstance(info.as_dict, Callable)


def test_Info__method_as_dict(testfile):
    info = Info(FLAC(testfile("vorbis/vorbis.flac")))
    assert len(info.as_dict()) == 7
    assert type(info.as_dict()) == dict
    assert info.bitrate == info.as_dict()["bitrate"]
    assert info.bits_per_sample == info.as_dict()["bits_per_sample"]
    assert info.channels == info.as_dict()["channels"]
    assert info.length == info.as_dict()["length"]
    assert info.mimetype == info.as_dict()["mimetype"]
    assert info.sample_rate == info.as_dict()["sample_rate"]
