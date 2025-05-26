from chess.components.pieces.abstract_piece import AbstractPiece
from chess.components.pieces import Pawn


def test_pawn() -> None:
    pawn = Pawn(AbstractPiece.BLACK)

    expected = pawn.unicode_map[AbstractPiece.BLACK]
    actual = pawn.get_symbol()

    assert expected == actual


def test_is_legal_move() -> None:
    pawn = Pawn(AbstractPiece.BLACK)
    assert pawn.is_legal_move((0, 0), (0, 1)) is True
