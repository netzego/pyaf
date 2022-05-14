from typing import Optional

from mutagen.id3 import (
    TALB,
    TIT2,
    TOPE,
    TPE2,
    TPOS,
    TRCK,
)


class Id3Core:
    # album
    @property
    def album(self) -> Optional[str]:
        if self._mutobj.tags and "TALB" in self._mutobj.tags:  # type: ignore
            return self._mutobj.tags.get("TALB").text[0]  # type: ignore

    @album.setter
    def album(self, value: str) -> None:
        self._mutobj.tags.add(TALB(encoding=3, text=[value]))  # type: ignore

    # albumartist
    @property
    def albumartist(self) -> Optional[str]:
        if self._mutobj.tags and "TPE2" in self._mutobj.tags:  # type: ignore
            return self._mutobj.tags.get("TPE2").text[0]  # type: ignore

    @albumartist.setter
    def albumartist(self, value: str) -> None:
        self._mutobj.tags.add(TPE2(encoding=3, text=[value]))  # type: ignore

    # artist
    @property
    def artist(self) -> Optional[str]:
        if self._mutobj.tags and "TOPE" in self._mutobj.tags:  # type: ignore
            return self._mutobj.tags.get("TOPE").text[0]  # type: ignore

    @artist.setter
    def artist(self, value: str) -> None:
        self._mutobj.tags.add(TOPE(encoding=3, text=[value]))  # type: ignore

    # title
    @property
    def title(self) -> Optional[str]:
        if self._mutobj.tags and "TIT2" in self._mutobj.tags:  # type: ignore
            return self._mutobj.tags.get("TIT2").text[0]  # type: ignore

    @title.setter
    def title(self, value: str) -> None:
        self._mutobj.tags.add(TIT2(encoding=3, text=[value]))  # type: ignore

    # discnumber
    @property
    def discnumber(self) -> Optional[int]:
        if self._mutobj.tags and "TPOS" in self._mutobj.tags:  # type: ignore
            return int(self._mutobj.tags.get("TPOS").text[0].split("/")[0])  # type: ignore

    @discnumber.setter
    def discnumber(self, value: int) -> None:
        self._mutobj.tags.add(TPOS(encoding=3, text=[f"{value}/{self.totaldisc}"]))  # type: ignore

    # totaldisc
    @property
    def totaldiscs(self) -> Optional[int]:
        if self._mutobj.tags and "TPOS" in self._mutobj.tags:  # type: ignore
            return int(self._mutobj.tags.get("TPOS").text[0].split("/")[1])  # type: ignore

    @totaldiscs.setter
    def totaldiscs(self, value: int) -> None:
        self._mutobj.tags.add(TPOS(encoding=3, text=[f"{self.discnumber}/{value}"]))  # type: ignore

    # tracknumber
    @property
    def tracknumber(self) -> Optional[int]:
        if self._mutobj.tags and "TRCK" in self._mutobj.tags:  # type: ignore
            return int(self._mutobj.tags.get("TRCK").text[0].split("/")[0])  # type: ignore

    @tracknumber.setter
    def tracknumber(self, value: int) -> None:
        self._mutobj.tags.add(TRCK(encoding=3, text=[f"{value}/{self.totaltrack}"]))  # type: ignore

    # totaltrack
    @property
    def totaltracks(self) -> Optional[int]:
        if self._mutobj.tags and "TRCK" in self._mutobj.tags:  # type: ignore
            return int(self._mutobj.tags.get("TRCK").text[0].split("/")[1])  # type: ignore

    @totaltracks.setter
    def totaltracks(self, value: int) -> None:
        self._mutobj.tags.add(TRCK(encoding=3, text=[f"{self.tracknumber}/{value}"]))  # type: ignore
