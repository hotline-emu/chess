from chess.components import PieceFactory
from chess.components.pieces import AbstractPiece, Rook, Bishop


def problem_scenario():
    black = AbstractPiece.BLACK
    white = AbstractPiece.WHITE

    grid = [  # Initialize everything to None.
        [None for _ in range(8)] for _ in range(8)
    ]

    # Initialize the scenario pieces.
    grid[2][5] = PieceFactory.create(Rook.lookup_name, black)
    grid[5][2] = PieceFactory.create(Bishop.lookup_name, white)

    return grid
