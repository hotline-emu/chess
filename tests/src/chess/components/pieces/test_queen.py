from chess.components.pieces import (
    AbstractPiece,
    Queen,
)


def test_queen() -> None:
    queen = Queen(AbstractPiece.BLACK)

    expected = queen.unicode_map[AbstractPiece.BLACK]
    actual = queen.get_symbol()

    assert expected == actual


def test_is_legal_move() -> None:
    queen = Queen(AbstractPiece.BLACK)
    assert queen.is_legal_move((0, 0), (0, 1)) is True
