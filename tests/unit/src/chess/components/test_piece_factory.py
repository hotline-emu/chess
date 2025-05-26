import pytest
from chess.components.pieces import PieceFactory
from chess.components.pieces.bishop import Bishop
from chess.exceptions import PieceNotFoundError


def test_create() -> None:
    kind = Bishop.lookup_name
    color = Bishop.BLACK

    actual = PieceFactory.create(kind, color)
    expected = Bishop(color)

    assert expected.lookup_name == actual.lookup_name


def test_create_not_found() -> None:
    kind = "foo"
    color = "bar"

    with pytest.raises(PieceNotFoundError):
        _ = PieceFactory.create(kind, color)
