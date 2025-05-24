from chess.exceptions import PieceNotFoundError
from .pieces import (
    AbstractPiece,
    Bishop,
    King,
    Knight,
    Pawn,
    Queen,
    Rook,
)


class PieceFactory:
    PIECES_MAP = {
        Bishop.lookup_name: Bishop,
        King.lookup_name: King,
        Knight.lookup_name: Knight,
        Pawn.lookup_name: Pawn,
        Queen.lookup_name: Queen,
        Rook.lookup_name: Rook,
    }

    @staticmethod
    def create(kind: str, color: str) -> AbstractPiece:
        piece_class = PieceFactory.PIECES_MAP.get(kind)
        if piece_class is None:
            raise PieceNotFoundError(kind)

        return piece_class(color, kind)
