from mutagen.id3 import (
    TALB,
    TIT2,
    TOPE,
    TPE2,
    TPOS,
    TRCK,
)


class Id3v2Core:
    # album
    @property
    def album(self) -> str:
        return self._mutobj.tags.get("TALB").text[0]  # type: ignore

    @album.setter
    def album(self, value: str) -> None:
        self._mutobj.tags.add(TALB(encoding=3, text=[value]))  # type: ignore

    # albumartist
    @property
    def albumartist(self) -> str:
        return self._mutobj.tags.get("TPE2").text[0]  # type: ignore

    @albumartist.setter
    def albumartist(self, value: str) -> None:
        self._mutobj.tags.add(TPE2(encoding=3, text=[value]))  # type: ignore

    # artist
    @property
    def artist(self) -> str:
        return self._mutobj.tags.get("TOPE").text[0]  # type: ignore

    @artist.setter
    def artist(self, value: str) -> None:
        self._mutobj.tags.add(TOPE(encoding=3, text=[value]))  # type: ignore

    # title
    @property
    def title(self) -> str:
        return self._mutobj.tags.get("TIT2").text[0]  # type: ignore

    @title.setter
    def title(self, value: str) -> None:
        self._mutobj.tags.add(TIT2(encoding=3, text=[value]))  # type: ignore

    # discnumber
    @property
    def discnumber(self) -> int:
        return int(self._mutobj.tags.get("TPOS").text[0].split("/")[0])  # type: ignore

    @discnumber.setter
    def discnumber(self, value: int) -> None:
        self._mutobj.tags.add(TPOS(encoding=3, text=[f"{value}/{self.totaldisc}"]))  # type: ignore

    # totaldisc
    @property
    def totaldisc(self) -> int:
        return int(self._mutobj.tags.get("TPOS").text[0].split("/")[1])  # type: ignore

    @totaldisc.setter
    def totaldisc(self, value: int) -> None:
        self._mutobj.tags.add(TPOS(encoding=3, text=[f"{self.discnumber}/{value}"]))  # type: ignore

    # tracknumber
    @property
    def tracknumber(self) -> int:
        return int(self._mutobj.tags.get("TRCK").text[0].split("/")[0])  # type: ignore

    @tracknumber.setter
    def tracknumber(self, value: int) -> None:
        self._mutobj.tags.add(TRCK(encoding=3, text=[f"{value}/{self.totaltrack}"]))  # type: ignore

    # totaltrack
    @property
    def totaltrack(self) -> int:
        return int(self._mutobj.tags.get("TRCK").text[0].split("/")[1])  # type: ignore

    @totaltrack.setter
    def totaltrack(self, value: int) -> None:
        self._mutobj.tags.add(TRCK(encoding=3, text=[f"{self.tracknumber}/{value}"]))  # type: ignore
