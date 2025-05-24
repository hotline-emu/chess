import pygame
from pygame import Surface
from pygame.event import Event
from chess.components import Board


class Engine:
    def __init__(self, display: Surface) -> None:
        self.board = Board()
        self.display = display
        self.selected_piece: tuple[int, int] | None = None

    def handle_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // self.board.tile_size
            row = y // self.board.tile_size

            if self.selected_piece:
                self.board.move_piece(self.selected_piece, (row, col))
                self.selected_piece = None
            elif self.board.get_piece((row, col)):
                self.selected_piece = (row, col)

    def update(self) -> None:
        pass  # Could later be used for animations or turn logic

    def draw(self) -> None:
        self.board.draw(self.display, self.selected_piece)
