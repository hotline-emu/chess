from unittest.mock import patch
import pytest
import pygame
from chess.game.engine import Engine


@pytest.fixture
def engine() -> Engine:
    rank_and_file_count = 8
    board_length = rank_and_file_count
    surface = pygame.display.set_mode((board_length, board_length))

    return Engine(surface)


@pytest.mark.usefixtures("init_pygame")
def test_init(engine: Engine) -> None:
    assert engine.selected_position is None


@pytest.mark.usefixtures("init_pygame")
def test_handle_event_select_piece(engine: Engine) -> None:
    file_mouse_position = 2
    rank_mouse_position = 1

    with patch.object(engine.board, "get_piece", return_value="pawn"):
        with patch(
            "pygame.mouse.get_pos",
            return_value=(
                engine.board.tile_size * file_mouse_position + 1,
                engine.board.tile_size * rank_mouse_position + 1,
            ),
        ):
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1)
            engine.handle_event(event)
            assert engine.selected_position == (rank_mouse_position, file_mouse_position)


@pytest.mark.usefixtures("init_pygame")
def test_handle_event_move_piece(engine: Engine) -> None:
    file_mouse_position = 3
    rank_mouse_position = 3
    target_position = (rank_mouse_position, file_mouse_position)

    origin_rank_position = 1
    origin_file_position = 2
    origin_position = (origin_rank_position, origin_file_position)

    engine.selected_position = (origin_rank_position, origin_file_position)

    with patch(
        "pygame.mouse.get_pos",
        return_value=(
            engine.board.tile_size * file_mouse_position + 1,
            engine.board.tile_size * rank_mouse_position + 1,
        ),
    ):
        with patch.object(engine.board, "move_piece") as patched_move_piece:
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1)
            engine.handle_event(event)
            patched_move_piece.assert_called_once_with(origin_position, target_position)
            assert engine.selected_position is None


@pytest.mark.usefixtures("init_pygame")
def test_draw(engine: Engine) -> None:
    with patch.object(engine.board, "draw") as patched_draw:
        selected_rank = 2
        selected_file = 3
        selected_position = (selected_rank, selected_file)

        engine.selected_position = selected_position
        engine.draw()

        patched_draw.assert_called_once_with(engine.display, selected_position)
