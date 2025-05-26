from chess.components.pieces.abstract_piece import AbstractPiece


class King(AbstractPiece):
    lookup_name = "king"
    unicode_map = {
        AbstractPiece.BLACK: "\u265a",
        AbstractPiece.WHITE: "\u2654",
    }

    def is_legal_move(
        self,
        initial_position: tuple[int, int],
        target_position: tuple[int, int],
    ) -> bool:
        return True
