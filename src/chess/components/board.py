from typing import Any
import pygame
from environs import env
from pygame import Surface
from chess.components import PieceFactory
from chess.components.pieces import (
    AbstractPiece,
    Bishop,
    King,
    Knight,
    Pawn,
    Queen,
    Rook,
)


class Board:
    def __init__(self) -> None:
        self.tile_size = env.int("tile_size")
        self.grid = self.create_initial_board()
        self.font = pygame.font.SysFont(
            env.str("font"),
            env.int("font_size"),
        )
        self.light_square_color = (235, 235, 208)
        self.dark_square_color = (119, 148, 85)
        self.selected_border_color = (255, 0, 0)
        self.black = (0, 0, 0)

    def draw(self, surface: Surface, selected: tuple[int, int] | None) -> None:
        colors = [self.light_square_color, self.dark_square_color]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                rect = pygame.Rect(
                    col * self.tile_size,
                    row * self.tile_size,
                    self.tile_size,
                    self.tile_size,
                )
                pygame.draw.rect(
                    surface=surface,
                    color=color,
                    rect=rect,
                )

                if selected == (row, col):
                    pygame.draw.rect(
                        surface=surface,
                        color=self.selected_border_color,
                        rect=rect,
                        width=3,
                    )

                piece: AbstractPiece = self.grid[row][col]
                if piece:
                    symbol = piece.get_symbol()
                    text_surface = self.font.render(  # Takes no keyword style args. Never seen that before.
                        symbol,  # Text
                        True,  # Antialias
                        self.black,  # Color
                    )
                    text_rect = text_surface.get_rect(center=rect.center)
                    surface.blit(
                        source=text_surface,
                        dest=text_rect,
                    )

    def create_initial_board(self) -> list[list[Any]]:
        board = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            board[1][i] = PieceFactory.create(Pawn.lookup_name, AbstractPiece.BLACK)
            board[6][i] = PieceFactory.create(Pawn.lookup_name, AbstractPiece.WHITE)

        board[0][0] = PieceFactory.create(Rook.lookup_name, AbstractPiece.BLACK)
        board[7][0] = PieceFactory.create(Rook.lookup_name, AbstractPiece.WHITE)
        board[0][7] = PieceFactory.create(Rook.lookup_name, AbstractPiece.BLACK)
        board[7][7] = PieceFactory.create(Rook.lookup_name, AbstractPiece.WHITE)

        board[0][1] = PieceFactory.create(Knight.lookup_name, AbstractPiece.BLACK)
        board[7][1] = PieceFactory.create(Knight.lookup_name, AbstractPiece.WHITE)
        board[0][6] = PieceFactory.create(Knight.lookup_name, AbstractPiece.BLACK)
        board[7][6] = PieceFactory.create(Knight.lookup_name, AbstractPiece.WHITE)

        board[0][2] = PieceFactory.create(Bishop.lookup_name, AbstractPiece.BLACK)
        board[7][2] = PieceFactory.create(Bishop.lookup_name, AbstractPiece.WHITE)
        board[0][5] = PieceFactory.create(Bishop.lookup_name, AbstractPiece.BLACK)
        board[7][5] = PieceFactory.create(Bishop.lookup_name, AbstractPiece.WHITE)

        board[0][3] = PieceFactory.create(Queen.lookup_name, AbstractPiece.BLACK)
        board[7][4] = PieceFactory.create(Queen.lookup_name, AbstractPiece.WHITE)

        board[0][4] = PieceFactory.create(King.lookup_name, AbstractPiece.BLACK)
        board[7][3] = PieceFactory.create(King.lookup_name, AbstractPiece.WHITE)

        return board

    def get_piece(self, position: tuple[int, int]) -> list[list[Any]]:
        row, column = position
        return self.grid[row][column]

    def move_piece(
        self,
        from_position: tuple[int, int],
        to_position: tuple[int, int],
    ) -> None:
        fx, fy = from_position
        tx, ty = to_position
        self.grid[tx][ty] = self.grid[fx][fy]
        self.grid[fx][fy] = None
