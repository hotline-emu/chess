from chess.components.pieces import (
    AbstractPiece,
    Pawn,
)


def test_pawn() -> None:
    pawn = Pawn(AbstractPiece.BLACK)

    expected = pawn.unicode_map[AbstractPiece.BLACK]
    actual = pawn.get_symbol()

    assert expected == actual
