from chess.components.pieces.abstract_piece import AbstractPiece
from chess.components.pieces import King


def test_king() -> None:
    king = King(AbstractPiece.BLACK)

    expected = king.unicode_map[AbstractPiece.BLACK]
    actual = king.get_symbol()

    assert expected == actual


def test_is_legal_move() -> None:
    king = King(AbstractPiece.BLACK)
    assert king.is_legal_move((0, 0), (0, 1)) is True
