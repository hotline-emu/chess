from chess.components.pieces import (
    AbstractPiece,
    King,
)


def test_king() -> None:
    king = King(AbstractPiece.BLACK)

    expected = king.unicode_map[AbstractPiece.BLACK]
    actual = king.get_symbol()

    assert expected == actual
