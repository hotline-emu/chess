from .abstract_piece import AbstractPiece


class Bishop(AbstractPiece):
    lookup_name = "bishop"
    unicode_map = {
        AbstractPiece.BLACK: "\u265d",
        AbstractPiece.WHITE: "\u2657",
    }

    def is_legal_move(
        self,
        initial_position: tuple[int, int],
        target_position: tuple[int, int],
    ) -> bool:
        initial_rank, initial_file = initial_position
        target_rank, target_file = target_position

        absolute_rank_differential = abs(target_rank - initial_rank)
        absolute_file_differential = abs(target_file - initial_file)
        move_is_not_diagonal = absolute_rank_differential != absolute_file_differential
        if move_is_not_diagonal:
            return False

        # TODO, Is blocked by friendly pieces OR enemery pieces prior to target destination.
        # Note: Not implemented yet, because the scenario in question does not have additional friendlies.

        return True
