from . import Piece


class PieceFactory:
    @staticmethod
    def create(kind: str, color: str) -> Piece:
        return Piece(color, kind)
