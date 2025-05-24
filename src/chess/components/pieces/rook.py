from .abstract_piece import AbstractPiece


class Rook(AbstractPiece):
    lookup_name = "rook"
    unicode_map = {
        AbstractPiece.BLACK: "\u265c",
        AbstractPiece.WHITE: "\u2656",
    }
