from .abstract_piece import AbstractPiece


class Bishop(AbstractPiece):
    lookup_name = "bishop"
    unicode_map = {
        AbstractPiece.BLACK: "\u265d",
        AbstractPiece.WHITE: "\u2657",
    }

    def is_legal_move(self, start_pos, end_pos, board):
        return True

        start_x, start_y = start_pos
        end_x, end_y = end_pos

        if abs(end_x - start_x) != abs(end_y - start_y):
            return False  # Not a diagonal move

        step_x = 1 if end_x > start_x else -1
        step_y = 1 if end_y > start_y else -1

        x, y = start_x + step_x, start_y + step_y
        while x != end_x and y != end_y:
            if board[x][y] is not None:
                return False
            x += step_x
            y += step_y

        return True
