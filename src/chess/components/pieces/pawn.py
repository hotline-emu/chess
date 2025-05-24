from .abstract_piece import AbstractPiece


class Pawn(AbstractPiece):
    lookup_name = "pawn"
    unicode_map = {
        AbstractPiece.BLACK: "\u265f",
        AbstractPiece.WHITE: "\u2659",
    }

    def is_legal_move(self, start_pos, end_pos, board):
        return True
