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

    def __init__(self, color: str) -> None:
        self.color = color

    def get_symbol(self) -> str:
        return str(self.unicode_map.get(self.color))

    @abstractmethod
    def is_legal_move(
        self,
        initial_position: tuple[int, int],
        target_position: tuple[int, int],
    ) -> bool:
        raise NotImplementedError()
