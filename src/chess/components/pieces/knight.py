from .abstract_piece import AbstractPiece


class Knight(AbstractPiece):
    lookup_name = "knight"
    unicode_map = {
        AbstractPiece.BLACK: "\u265e",
        AbstractPiece.WHITE: "\u2658",
    }

    def is_legal_move(self, start_pos, end_pos, board): ...
