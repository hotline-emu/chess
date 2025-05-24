from chess.components.pieces import (
    AbstractPiece,
    Bishop,
)


def test_bishop() -> None:
    bishop = Bishop(AbstractPiece.BLACK)

    expected = bishop.unicode_map[AbstractPiece.BLACK]
    actual = bishop.get_symbol()

    assert expected == actual
