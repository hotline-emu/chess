from chess.components.pieces.abstract_piece import AbstractPiece


class Knight(AbstractPiece):
    lookup_name = "knight"
    unicode_map = {
        AbstractPiece.BLACK: "\u265e",
        AbstractPiece.WHITE: "\u2658",
    }

    def is_legal_move(
        self,
        initial_position: tuple[int, int],
        target_position: tuple[int, int],
    ) -> bool:
        return True
