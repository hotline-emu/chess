import pygame
from pygame import Surface
from pygame.event import Event
from chess.board import Board


class ChessGame:
    def __init__(self, screen: Surface) -> None:
        self.board = Board()
        self.screen = screen
        self.selected: tuple[int, int] | None = None

    def handle_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // self.board.tile_size
            row = y // self.board.tile_size

            if self.selected:
                self.board.move_piece(self.selected, (row, col))
                self.selected = None
            elif self.board.get_piece((row, col)):
                self.selected = (row, col)

    def update(self) -> None:
        pass  # Could later be used for animations or turn logic

    def draw(self) -> None:
        self.board.draw(self.screen, self.selected)
