class PieceNotFoundError(Exception):
    def __init__(self, kind: str) -> None:
        message = f"Piece of kind type '{kind}' not found"
        super().__init__(message)
