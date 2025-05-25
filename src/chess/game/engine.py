import pygame
from pygame import Surface
from pygame.font import Font
from pygame.event import Event
from chess.components import Board
from chess.components.pieces import AbstractPiece


class Engine:
    def __init__(self, display: Surface, scenario: str | None = None) -> None:
        self.board = Board(scenario)
        self.display = display
        self.selected_position: tuple[int, int] | None = None

    def handle_event(self, event: Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            file = x // self.board.tile_size
            rank = y // self.board.tile_size
            target_position = (rank, file)

            if self.selected_position:
                piece: AbstractPiece = self.board.get_piece(self.selected_position)
                if not piece.is_legal_move(self.selected_position, target_position):
                    self.__show_illegal_move_message(self.display, self.board.font)
                    self.selected_position = None
                    return  # Skip the move

                self.board.move_piece(self.selected_position, target_position)
                self.selected_position = None
            elif self.board.get_piece(target_position):
                self.selected_position = target_position

    def update(self) -> None: ...  # Reserved for turn logic IFF necessary.

    def draw(self) -> None:
        self.board.draw(self.display, self.selected_position)

    def __show_illegal_move_message(self, surface: Surface, font: Font) -> None:
        text = font.render("Illegal Move!", True, (255, 0, 0))
        surface.blit(text, (10, 10))
        pygame.display.update()
        one_second = 1000
        pygame.time.wait(one_second)
