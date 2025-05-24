import pytest
import pygame
from chess.game.engine import Engine


@pytest.mark.usefixtures("init_pygame")
def test_init() -> None:
    row_and_column_count = 8
    board_length = row_and_column_count
    surface = pygame.display.set_mode((board_length, board_length))
    engine = Engine(surface)

    assert engine.selected_piece is None
