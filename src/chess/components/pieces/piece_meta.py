from abc import ABCMeta
from types import MappingProxyType
from typing import Any, Tuple, Type


class PieceMeta(ABCMeta):
    def __new__(
        mcs: Type[type],
        name: str,
        bases: Tuple[type, ...],
        namespace: MappingProxyType[str, Any],
    ) -> type:
        cls = super().__new__(mcs, name, bases, namespace)

        if not getattr(cls, "__abstractmethods__", None):
            if not hasattr(cls, "lookup_name"):
                raise TypeError(
                    f"Class '{name}' must define class attribute 'lookup_name'"
                )

        return cls
