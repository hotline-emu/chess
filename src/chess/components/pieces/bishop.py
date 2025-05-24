from .abstract_piece import AbstractPiece


class Bishop(AbstractPiece):
    lookup_name = "bishop"
    unicode_map = {
        AbstractPiece.BLACK: "\u265d",
        AbstractPiece.WHITE: "\u2657",
    }
