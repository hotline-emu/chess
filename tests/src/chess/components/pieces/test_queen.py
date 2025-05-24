from chess.components.pieces import (
    AbstractPiece,
    Queen,
)


def test_queen() -> None:
    queen = Queen(AbstractPiece.BLACK)

    expected = queen.unicode_map[AbstractPiece.BLACK]
    actual = queen.get_symbol()

    assert expected == actual
