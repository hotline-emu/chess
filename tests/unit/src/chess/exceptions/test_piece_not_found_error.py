from chess.exceptions import PieceNotFoundError


def test_exception() -> None:
    piece_type = "foo"
    exception = PieceNotFoundError(piece_type)

    expected = f"Piece of kind type '{piece_type}' not found"
    actual = str(exception)

    assert expected == actual
