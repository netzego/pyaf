from typing import Optional


class VorbisCore:
    # album
    @property
    def album(self) -> Optional[str]:
        if "ALBUM" in self._mutobj.tags:  # type: ignore
            return self._mutobj.tags["ALBUM"][0]  # type: ignore

    @album.setter
    def album(self, value: str) -> None:
        self._mutobj.tags["ALBUM"] = [value]  # type: ignore

    # albumartist
    @property
    def albumartist(self) -> Optional[str]:
        if "ALBUMARTIST" in self._mutobj.tags:  # type: ignore
            return self._mutobj.tags["ALBUMARTIST"][0]  # type: ignore

    @albumartist.setter
    def albumartist(self, value: str) -> None:
        self._mutobj.tags["ALBUMARTIST"] = [value]  # type: ignore

    # artist
    @property
    def artist(self) -> Optional[str]:
        if "ARTIST" in self._mutobj.tags:  # type: ignore
            return self._mutobj.tags["ARTIST"][0]  # type: ignore

    @artist.setter
    def artist(self, value: str) -> None:
        self._mutobj.tags["ARTIST"] = [value]  # type: ignore

    # title
    @property
    def title(self) -> Optional[str]:
        if "TITLE" in self._mutobj.tags:  # type: ignore
            return self._mutobj.tags["TITLE"][0]  # type: ignore

    @title.setter
    def title(self, value: str) -> None:
        self._mutobj.tags["TITLE"] = [value]  # type: ignore

    # tracknumber
    @property
    def tracknumber(self) -> Optional[int]:
        if "TRACKNUMBER" in self._mutobj.tags:  # type: ignore
            return int(self._mutobj.tags["TRACKNUMBER"][0])  # type: ignore

    @tracknumber.setter
    def tracknumber(self, value: int) -> None:
        self._mutobj.tags["TRACKNUMBER"] = [str(value)]  # type: ignore

    # totaltracks
    @property
    def totaltracks(self) -> Optional[int]:
        if "TOTALTRACKS" in self._mutobj.tags:  # type: ignore
            return int(self._mutobj.tags["TOTALTRACKS"][0])  # type: ignore

    @totaltracks.setter
    def totaltracks(self, value: int) -> None:
        self._mutobj.tags["TOTALTRACKS"] = [str(value)]  # type: ignore

    # discnumber
    @property
    def discnumber(self) -> Optional[int]:
        if "DISCNUMBER" in self._mutobj.tags:  # type: ignore
            return int(self._mutobj.tags["DISCNUMBER"][0])  # type: ignore

    @discnumber.setter
    def discnumber(self, value: int) -> None:
        self._mutobj.tags["DISCNUMBER"] = [str(value)]  # type: ignore

    # totaldisccs
    @property
    def totaldiscs(self) -> Optional[int]:
        if "TOTALDISCS" in self._mutobj.tags:  # type: ignore
            return int(self._mutobj.tags["TOTALDISCS"][0])  # type: ignore

    @totaldiscs.setter
    def totaldiscs(self, value: int) -> None:
        self._mutobj.tags["TOTALDISCS"] = [str(value)]  # type: ignore
