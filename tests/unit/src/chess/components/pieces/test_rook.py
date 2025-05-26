from chess.components.pieces.abstract_piece import AbstractPiece
from chess.components.pieces import Rook


def test_rook() -> None:
    rook = Rook(AbstractPiece.BLACK)

    expected = rook.unicode_map[AbstractPiece.BLACK]
    actual = rook.get_symbol()

    assert expected == actual


def test_is_legal_move_return_true() -> None:
    rook = Rook(AbstractPiece.BLACK)
    assert rook.is_legal_move((0, 0), (1, 0)) is True


def test_is_legal_move_return_false() -> None:
    rook = Rook(AbstractPiece.BLACK)
    assert rook.is_legal_move((0, 0), (1, 1)) is False
