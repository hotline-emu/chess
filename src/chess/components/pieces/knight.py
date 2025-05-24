from .abstract_piece import AbstractPiece


class Knight(AbstractPiece):
    lookup_name = "knight"
    unicode_map = {
        AbstractPiece.BLACK: "\u265e",
        AbstractPiece.WHITE: "\u2658",
    }
