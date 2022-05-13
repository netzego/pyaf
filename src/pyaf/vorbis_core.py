class VorbisCore:
    # album
    @property
    def album(self) -> str:
        return self._mutobj.tags["ALBUM"][0]  # type: ignore

    @album.setter
    def album(self, value: str) -> None:
        self._mutobj.tags["ALBUM"] = [value]  # type: ignore

    # albumartist
    @property
    def albumartist(self) -> str:
        return self._mutobj.tags["ALBUMARTIST"][0]  # type: ignore

    @albumartist.setter
    def albumartist(self, value: str) -> None:
        self._mutobj.tags["ALBUMARTIST"] = [value]  # type: ignore

    # artist
    @property
    def artist(self) -> str:
        return self._mutobj.tags["ARTIST"][0]  # type: ignore

    @artist.setter
    def artist(self, value: str) -> None:
        self._mutobj.tags["ARTIST"] = [value]  # type: ignore

    # title
    @property
    def title(self) -> str:
        return self._mutobj.tags["TITLE"][0]  # type: ignore

    @title.setter
    def title(self, value: str) -> None:
        self._mutobj.tags["TITLE"] = [value]  # type: ignore

    # tracknumber
    @property
    def tracknumber(self) -> int:
        return self._mutobj.tags["TRACKNUMBER"][0]  # type: ignore

    @tracknumber.setter
    def tracknumber(self, value: int) -> None:
        self._mutobj.tags["TRACKNUMBER"] = [value]  # type: ignore

    # totaltracks
    @property
    def totaltracks(self) -> int:
        return self._mutobj.tags["TOTALTRACKS"][0]  # type: ignore

    @totaltracks.setter
    def totaltracks(self, value: int) -> None:
        self._mutobj.tags["TOTALTRACKS"] = [value]  # type: ignore

    # discnumber
    @property
    def discnumber(self) -> int:
        return self._mutobj.tags["DISCNUMBER"][0]  # type: ignore

    @discnumber.setter
    def discnumber(self, value: int) -> None:
        self._mutobj.tags["DISCNUMBER"] = [value]  # type: ignore

    # totaldisccs
    @property
    def totaldiscs(self) -> int:
        return self._mutobj.tags["TOTALDISCS"][0]  # type: ignore

    @totaldiscs.setter
    def totaldiscs(self, value: int) -> None:
        self._mutobj.tags["TOTALDISCS"] = [value]  # type: ignore
