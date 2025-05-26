from unittest.mock import patch
import pytest
import pygame
from chess.game.engine import Engine


@pytest.fixture
def engine() -> Engine:
    rank_and_file_count = 8
    board_length = rank_and_file_count
    surface = pygame.display.set_mode((board_length, board_length))
    scenario = "the_setup"

    return Engine(surface, scenario)


@pytest.mark.usefixtures("init_pygame")
def test_can_bishop_capture_rook(engine: Engine) -> None:
    # Bishop starts here.
    bishop_origin_rank_position = 5
    bishop_origin_file_position = 2
    engine.selected_position = (
        bishop_origin_rank_position,
        bishop_origin_file_position,
    )

    # Bishop wants to go here.
    rook_rank_mouse_position = 2
    rook_file_mouse_position = 5

    # Patch to simulate the mouse click.
    with patch(
        "pygame.mouse.get_pos",
        return_value=(
            engine.board.tile_size * rook_file_mouse_position + 1,
            engine.board.tile_size * rook_rank_mouse_position + 1,
        ),
    ):
        with patch.object(engine, "_Engine__show_illegal_move_message") as patched_show_illegal_move_message:
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1)
            engine.handle_event(event)
            patched_show_illegal_move_message.assert_not_called()  # Because the move is legal.


@pytest.mark.usefixtures("init_pygame")
def test_can_rook_capture_bishop(engine: Engine) -> None:
    # Rook starts here.
    rook_origin_rank_position = 2
    rook_origin_file_position = 5
    engine.selected_position = (
        rook_origin_rank_position,
        rook_origin_file_position,
    )

    # Rook wants to go here.
    bishop_rank_mouse_position = 5
    bishop_file_mouse_position = 2

    # Patch to simulate the mouse click.
    with patch(
        "pygame.mouse.get_pos",
        return_value=(
            engine.board.tile_size * bishop_file_mouse_position + 1,
            engine.board.tile_size * bishop_rank_mouse_position + 1,
        ),
    ):
        with patch.object(engine, "_Engine__show_illegal_move_message") as patched_show_illegal_move_message:
            event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1)
            engine.handle_event(event)
            patched_show_illegal_move_message.assert_called_once()  # Because the move is illegal.
