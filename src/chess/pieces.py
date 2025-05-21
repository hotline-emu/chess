class Piece:
    def __init__(self, color: str, kind: str) -> None:
        self.color = color
        self.kind = kind


class PieceFactory:
    @staticmethod
    def create(kind: str, color: str) -> Piece:
        return Piece(color, kind)
