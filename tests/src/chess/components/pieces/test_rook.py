from chess.components.pieces import (
    AbstractPiece,
    Rook,
)


def test_rook() -> None:
    rook = Rook(AbstractPiece.BLACK)

    expected = rook.unicode_map[AbstractPiece.BLACK]
    actual = rook.get_symbol()

    assert expected == actual
