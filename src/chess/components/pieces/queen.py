from .abstract_piece import AbstractPiece


class Queen(AbstractPiece):
    lookup_name = "queen"
    unicode_map = {
        AbstractPiece.BLACK: "\u265b",
        AbstractPiece.WHITE: "\u2655",
    }

    def is_legal_move(self, start_pos, end_pos, board): ...
