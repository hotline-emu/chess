from chess.components.pieces import (
    AbstractPiece,
    Knight,
)


def test_knight() -> None:
    knight = Knight(AbstractPiece.BLACK)

    expected = knight.unicode_map[AbstractPiece.BLACK]
    actual = knight.get_symbol()

    assert expected == actual
