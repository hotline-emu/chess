from .abstract_piece import AbstractPiece


class Rook(AbstractPiece):
    lookup_name = "rook"
    unicode_map = {
        AbstractPiece.BLACK: "\u265c",
        AbstractPiece.WHITE: "\u2656",
    }

    def is_legal_move(self, initial_position, target_position, board):
        initial_rank, initial_file = initial_position
        target_rank, target_file = target_position

        file_and_rank_both_changed = (
            initial_file != target_file and initial_rank != target_rank
        )
        if file_and_rank_both_changed:
            # Must move in a straight line.
            # Both cannot have changed.
            return False

        # TODO, is blocked?

        return True
