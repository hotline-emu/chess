from .abstract_piece import AbstractPiece


class Rook(AbstractPiece):
    lookup_name = "rook"
    unicode_map = {
        AbstractPiece.BLACK: "\u265c",
        AbstractPiece.WHITE: "\u2656",
    }

    def is_legal_move(self, start_pos, end_pos, board):
        return True

        start_x, start_y = start_pos
        end_x, end_y = end_pos

        if start_x != end_x and start_y != end_y:
            return False  # Must move in a straight line

        # Check path is clear
        if start_x == end_x:
            step = 1 if end_y > start_y else -1
            for y in range(start_y + step, end_y, step):
                if board[start_x][y] is not None:
                    return False
        else:
            step = 1 if end_x > start_x else -1
            for x in range(start_x + step, end_x, step):
                if board[x][start_y] is not None:
                    return False

        return True
