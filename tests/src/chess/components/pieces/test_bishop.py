from chess.components.pieces import (
    AbstractPiece,
    Bishop,
)


def test_bishop() -> None:
    bishop = Bishop(AbstractPiece.BLACK)

    expected = bishop.unicode_map[AbstractPiece.BLACK]
    actual = bishop.get_symbol()

    assert expected == actual


def test_is_legal_move_return_true() -> None:
    bishop = Bishop(AbstractPiece.BLACK)
    assert bishop.is_legal_move((0, 0), (1, 1)) is True


def test_is_legal_move_return_false() -> None:
    bishop = Bishop(AbstractPiece.BLACK)
    assert bishop.is_legal_move((0, 0), (1, 0)) is False
