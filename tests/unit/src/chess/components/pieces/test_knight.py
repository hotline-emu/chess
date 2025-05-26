from chess.components.pieces.abstract_piece import AbstractPiece
from chess.components.pieces import Knight


def test_knight() -> None:
    knight = Knight(AbstractPiece.BLACK)

    expected = knight.unicode_map[AbstractPiece.BLACK]
    actual = knight.get_symbol()

    assert expected == actual


def test_is_legal_move() -> None:
    knight = Knight(AbstractPiece.BLACK)
    assert knight.is_legal_move((0, 0), (0, 1)) is True
