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
        self.rank_and_file_count = 8
        self.grid = self.__create_initial_board()
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
        for rank in range(self.rank_and_file_count):
            for file in range(self.rank_and_file_count):
                color = colors[(rank + file) % 2]
                rect = pygame.Rect(
                    file * self.tile_size,
                    rank * self.tile_size,
                    self.tile_size,
                    self.tile_size,
                )
                pygame.draw.rect(
                    surface=surface,
                    color=color,
                    rect=rect,
                )

                if selected == (rank, file):
                    pygame.draw.rect(
                        surface=surface,
                        color=self.selected_border_color,
                        rect=rect,
                        width=3,
                    )

                piece: AbstractPiece = self.grid[rank][file]
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

        self.__draw_labels(surface)

    def __draw_labels(self, screen):
        label_padding = 15
        label_font = pygame.font.SysFont("Arial", 16)
        antialias = True
        font_color = (0, 0, 0)

        # Draw numbers 8 to 1 (ranks) on the left side
        for rank in range(self.rank_and_file_count):
            label_text = str(8 - rank)
            label = label_font.render(
                label_text,
                antialias,
                font_color,
            )

            x_coordinate = label_padding // 2 - label.get_width() // 2
            y_coordinate = (
                rank * self.tile_size + self.tile_size // 2 - label.get_height() // 2
            )
            destination = (x_coordinate, y_coordinate)
            screen.blit(label, destination)

        # Draw letters a to h (files) at the bottom
        for file in range(self.rank_and_file_count):
            label_text = chr(ord("a") + file)
            label = label_font.render(
                label_text,
                antialias,
                font_color,
            )
            x_coordinate = (
                file * self.tile_size
                + label_padding
                + self.tile_size // 2
                - label.get_width() // 2
            ) - 15
            y_coordinate = (
                self.rank_and_file_count * self.tile_size
            ) - 20
            destination = (x_coordinate, y_coordinate)
            screen.blit(label, destination)

    def get_piece(self, position: tuple[int, int]) -> list[list[Any]]:
        rank, file = position
        return self.grid[rank][file]

    def move_piece(
        self,
        from_position: tuple[int, int],
        to_position: tuple[int, int],
    ) -> None:
        from_rank, from_file = from_position
        to_rank, to_file = to_position
        self.grid[to_rank][to_file] = self.grid[from_rank][from_file]
        self.grid[from_rank][from_file] = None

    def __create_initial_board(self) -> list[list[Any]]:
        black = AbstractPiece.BLACK
        white = AbstractPiece.WHITE

        board = [  # Initialize everything to None.
            [None for _ in range(self.rank_and_file_count)]
            for _ in range(self.rank_and_file_count)
        ]

        # Initialize the pawn ranks.
        for file_index in range(self.rank_and_file_count):
            black_pawn_rank = 1
            white_pawn_rank = 6
            board[black_pawn_rank][file_index] = PieceFactory.create(
                Pawn.lookup_name,
                black,
            )
            board[white_pawn_rank][file_index] = PieceFactory.create(
                Pawn.lookup_name,
                white,
            )

        # Initialize the rest of the pieces below.
        board[0][0] = PieceFactory.create(Rook.lookup_name, black)
        board[7][0] = PieceFactory.create(Rook.lookup_name, white)
        board[0][7] = PieceFactory.create(Rook.lookup_name, black)
        board[7][7] = PieceFactory.create(Rook.lookup_name, white)

        board[0][1] = PieceFactory.create(Knight.lookup_name, black)
        board[7][1] = PieceFactory.create(Knight.lookup_name, white)
        board[0][6] = PieceFactory.create(Knight.lookup_name, black)
        board[7][6] = PieceFactory.create(Knight.lookup_name, white)

        board[0][2] = PieceFactory.create(Bishop.lookup_name, black)
        board[7][2] = PieceFactory.create(Bishop.lookup_name, white)
        board[0][5] = PieceFactory.create(Bishop.lookup_name, black)
        board[7][5] = PieceFactory.create(Bishop.lookup_name, white)

        board[0][3] = PieceFactory.create(Queen.lookup_name, black)
        board[7][4] = PieceFactory.create(Queen.lookup_name, white)

        board[0][4] = PieceFactory.create(King.lookup_name, black)
        board[7][3] = PieceFactory.create(King.lookup_name, white)

        return board
