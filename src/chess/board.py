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
                "k": "\u2654",
                "q": "\u2655",
                "r": "\u2656",
                "b": "\u2657",
                "n": "\u2658",
                "p": "\u2659",
            },
            "black": {
                "k": "\u265a",
                "q": "\u265b",
                "r": "\u265c",
                "b": "\u265d",
                "n": "\u265e",
                "p": "\u265f",
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
            board[1][i] = PieceFactory.create("p", "black")
            board[6][i] = PieceFactory.create("p", "white")
        # TODO: Add other pieces
        return board

    def get_piece(self, pos: tuple[int, int]) -> list[list[Any]]:
        row, col = pos
        return self.grid[row][col]

    def move_piece(self, from_pos: tuple[int, int], to_pos: tuple[int, int]) -> None:
        fx, fy = from_pos
        tx, ty = to_pos
        self.grid[tx][ty] = self.grid[fx][fy]
        self.grid[fx][fy] = None
