from os import path


def test_empty(testfiles_empty):
    for f in testfiles_empty:
        assert path.isfile(f) == True


def test_notags(testfiles_notags):
    for f in testfiles_notags:
        assert path.isfile(f) == True


def test_id3v1(testfiles_id3v1):
    for f in testfiles_id3v1:
        assert path.isfile(f) == True


def test_id3v2(testfiles_id3v2):
    for f in testfiles_id3v2:
        assert path.isfile(f) == True


def test_vorbis(testfiles_vorbis):
    for f in testfiles_vorbis:
        assert path.isfile(f) == True


def test_perm(testfiles_perm):
    for f in testfiles_perm:
        assert path.isfile(f) == True


def test_ext(testfiles_perm):
    for f in testfiles_perm:
        assert path.isfile(f) == True


def test_symlink(testfiles_symlink):
    for f in testfiles_symlink:
        assert path.exists(f) == True
        assert path.islink(f) == True


def test_corrupt(testfiles_perm):
    for f in testfiles_perm:
        assert path.isfile(f) == True


# TODO: recursiv
