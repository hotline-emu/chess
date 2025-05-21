from typing import Any
import pygame
from environs import env
from pygame import Surface
from chess.pieces import PieceFactory


class Board:
    def __init__(self) -> None:
        self.tile_size = env.int("tile_size")
        self.grid = self.create_initial_board()
        self.font = pygame.font.SysFont(
            env.str("font"),
            env.int("font_size"),
        )

        self.unicode_map = {
            "white": {
                "king": "\u2654",
                "queen": "\u2655",
                "rook": "\u2656",
                "bishop": "\u2657",
                "knight": "\u2658",
                "pawn": "\u2659",
            },
            "black": {
                "king": "\u265a",
                "queen": "\u265b",
                "rook": "\u265c",
                "bishop": "\u265d",
                "knight": "\u265e",
                "pawn": "\u265f",
            },
        }

    def draw(self, screen: Surface, selected: tuple[int, int] | None) -> None:
        colors = [(235, 235, 208), (119, 148, 85)]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                rect = pygame.Rect(
                    col * self.tile_size,
                    row * self.tile_size,
                    self.tile_size,
                    self.tile_size,
                )
                pygame.draw.rect(screen, color, rect)

                if selected == (row, col):
                    pygame.draw.rect(screen, (255, 0, 0), rect, 3)

                piece = self.grid[row][col]
                if piece:
                    symbol = self.unicode_map[piece.color][piece.kind]
                    text_surface = self.font.render(symbol, True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=rect.center)
                    screen.blit(text_surface, text_rect)

    def create_initial_board(self) -> list[list[Any]]:
        board = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            board[1][i] = PieceFactory.create("pawn", "black")
            board[6][i] = PieceFactory.create("pawn", "white")

        board[0][0] = PieceFactory.create("rook", "black")
        board[7][0] = PieceFactory.create("rook", "white")
        board[0][7] = PieceFactory.create("rook", "black")
        board[7][7] = PieceFactory.create("rook", "white")

        board[0][1] = PieceFactory.create("knight", "black")
        board[7][1] = PieceFactory.create("knight", "white")
        board[0][6] = PieceFactory.create("knight", "black")
        board[7][6] = PieceFactory.create("knight", "white")

        board[0][2] = PieceFactory.create("bishop", "black")
        board[7][2] = PieceFactory.create("bishop", "white")
        board[0][5] = PieceFactory.create("bishop", "black")
        board[7][5] = PieceFactory.create("bishop", "white")

        board[0][3] = PieceFactory.create("queen", "black")
        board[7][4] = PieceFactory.create("queen", "white")

        board[0][4] = PieceFactory.create("king", "black")
        board[7][3] = PieceFactory.create("king", "white")

        return board

    def get_piece(self, pos: tuple[int, int]) -> list[list[Any]]:
        row, col = pos
        return self.grid[row][col]

    def move_piece(self, from_pos: tuple[int, int], to_pos: tuple[int, int]) -> None:
        fx, fy = from_pos
        tx, ty = to_pos
        self.grid[tx][ty] = self.grid[fx][fy]
        self.grid[fx][fy] = None
