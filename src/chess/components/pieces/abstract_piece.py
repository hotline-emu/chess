from abc import ABC
from typing import Any, Type


class AbstractPiece(ABC):
    def __init__(self, color: str, kind: str) -> None:
        self.color = color
        self.kind = kind

    def __init_subclass__(cls: Type["AbstractPiece"], **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "lookup_name"):
            raise TypeError(
                f"Class '{cls.__name__}' must define class attribute 'lookup_name'"
            )
