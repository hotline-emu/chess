from typing import Any
from chess.components import PieceFactory
from chess.components.pieces import AbstractPiece, Rook, Bishop

BLACK = AbstractPiece.BLACK
WHITE = AbstractPiece.WHITE

def setup_scenario() -> list[list[Any]]:

    grid = [  # Initialize everything to None.
        [None for _ in range(8)] for _ in range(8)
    ]

    # Initialize the scenario pieces.
    grid[2][5] = PieceFactory.create(Rook.lookup_name, BLACK)
    grid[5][2] = PieceFactory.create(Bishop.lookup_name, WHITE)

    return grid


def problem_scenario() -> list[list[Any]]:

    grid = [  # Initialize everything to None.
        [None for _ in range(8)] for _ in range(8)
    ]

    # Initialize the scenario pieces.
    grid[5][2] = PieceFactory.create(Bishop.lookup_name, BLACK)
    grid[7][7] = PieceFactory.create(Rook.lookup_name, WHITE)

    return grid
