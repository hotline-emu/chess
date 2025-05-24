from unittest.mock import patch
import pytest
import pygame
from chess.game.engine import Engine


@pytest.fixture
def engine():
    row_and_column_count = 8
    board_length = row_and_column_count
    surface = pygame.display.set_mode((board_length, board_length))

    return Engine(surface)


@pytest.mark.usefixtures("init_pygame")
def test_init(engine) -> None:
    assert engine.selected_piece is None


@pytest.mark.usefixtures("init_pygame")
def test_handle_event_select_piece(engine):
    with patch.object(engine.board, "get_piece", return_value="pawn"):
        with patch(
            "pygame.mouse.get_pos",
            return_value=(
                engine.board.tile_size * 2 + 1,
                engine.board.tile_size * 1 + 1,
            ),
        ):
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1)
            engine.handle_event(event)
            assert engine.selected_piece == (1, 2)


@pytest.mark.usefixtures("init_pygame")
def test_handle_event_move_piece(engine):
    engine.selected_piece = (1, 2)

    # Mock position to move to
    new_pos = (3, 3)
    with patch(
        "pygame.mouse.get_pos",
        return_value=(
            engine.board.tile_size * new_pos[1] + 1,
            engine.board.tile_size * new_pos[0] + 1,
        ),
    ):
        with patch.object(engine.board, "move_piece") as move_mock:
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1)
            engine.handle_event(event)
            move_mock.assert_called_once_with((1, 2), new_pos)
            assert engine.selected_piece is None


@pytest.mark.usefixtures("init_pygame")
def test_draw(engine):
    with patch.object(engine.board, "draw") as draw_mock:
        engine.selected_piece = (2, 3)
        engine.draw()
        draw_mock.assert_called_once_with(engine.display, (2, 3))
