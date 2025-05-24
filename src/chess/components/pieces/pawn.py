from .abstract_piece import AbstractPiece


class Pawn(AbstractPiece):
    lookup_name = "pawn"
    unicode_map = {
        AbstractPiece.BLACK: "\u265f",
        AbstractPiece.WHITE: "\u2659",
    }
