from .abstract_piece import AbstractPiece


class Bishop(AbstractPiece):
    lookup_name = "bishop"
    unicode_map = {
        AbstractPiece.BLACK: "\u265d",
        AbstractPiece.WHITE: "\u2657",
    }

    def is_legal_move(self, initial_position, target_position, board):
        initial_rank, initial_file = initial_position
        target_rank, target_file = target_position

        absolute_rank_differential = abs(target_rank - initial_rank)
        absolute_file_differential = abs(target_file - initial_file)
        move_is_not_diagonal = absolute_rank_differential != absolute_file_differential
        if move_is_not_diagonal:
            return False

        # TODO, is blocked?

        return True
