class Piece:
    def __init__(self, color: str, kind: str) -> None:
        self.color = color  # 'white' or 'black'
        self.kind = kind  # 'p', 'r', 'n', etc.


class PieceFactory:
    @staticmethod
    def create(kind: str, color: str) -> Piece:
        return Piece(color, kind)
