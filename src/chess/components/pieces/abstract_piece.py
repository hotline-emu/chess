from abc import ABC, abstractmethod


class AbstractPiece(ABC):
    BLACK = "black"
    WHITE = "white"

    @property
    @abstractmethod
    def lookup_name(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def unicode_map(self) -> dict[str, str]:
        raise NotImplementedError()

    def __init__(self, color: str, kind: str) -> None:
        self.color = color
        self.kind = kind

    def get_symbol(self) -> str:
        return str(self.unicode_map.get(self.color))
