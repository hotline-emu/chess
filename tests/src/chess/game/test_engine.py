from unittest.mock import patch
import pytest
import pygame
from chess.game.engine import Engine


@pytest.fixture
def engine() -> Engine:
    row_and_column_count = 8
    board_length = row_and_column_count
    surface = pygame.display.set_mode((board_length, board_length))

    return Engine(surface)


@pytest.mark.usefixtures("init_pygame")
def test_init(engine: Engine) -> None:
    assert engine.selected_piece is None


@pytest.mark.usefixtures("init_pygame")
def test_handle_event_select_piece(engine: Engine) -> None:
    column_mouse_position = 2
    row_mouse_position = 1

    with patch.object(engine.board, "get_piece", return_value="pawn"):
        with patch(
            "pygame.mouse.get_pos",
            return_value=(
                engine.board.tile_size * column_mouse_position + 1,
                engine.board.tile_size * row_mouse_position + 1,
            ),
        ):
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1)
            engine.handle_event(event)
            assert engine.selected_piece == (row_mouse_position, column_mouse_position)


@pytest.mark.usefixtures("init_pygame")
def test_handle_event_move_piece(engine: Engine) -> None:
    column_mouse_position = 3
    row_mouse_position = 3
    target_position = (row_mouse_position, column_mouse_position)

    origin_row_position = 1
    origin_column_position = 2
    origin_position = (origin_row_position, origin_column_position)

    engine.selected_piece = (origin_row_position, origin_column_position)

    with patch(
        "pygame.mouse.get_pos",
        return_value=(
            engine.board.tile_size * column_mouse_position + 1,
            engine.board.tile_size * row_mouse_position + 1,
        ),
    ):
        with patch.object(engine.board, "move_piece") as patched_move_piece:
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1)
            engine.handle_event(event)
            patched_move_piece.assert_called_once_with(origin_position, target_position)
            assert engine.selected_piece is None


@pytest.mark.usefixtures("init_pygame")
def test_draw(engine: Engine) -> None:
    with patch.object(engine.board, "draw") as patched_draw:
        selected_row = 2
        selected_column = 3
        selected_position = (selected_row, selected_column)

        engine.selected_piece = selected_position
        engine.draw()

        patched_draw.assert_called_once_with(engine.display, selected_position)
