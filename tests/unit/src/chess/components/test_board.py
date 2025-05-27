from unittest.mock import patch, MagicMock
import pytest
import pygame
from chess.components import Board
from chess.components.pieces import Rook, Pawn


@pytest.mark.usefixtures("init_pygame")
def test_get_piece() -> None:
    board = Board()

    top_leftmost_piece = (0, 0)
    actual: Rook = board.get_piece(top_leftmost_piece)

    assert actual.lookup_name == Rook.lookup_name
    assert actual.color == Rook.BLACK


@pytest.mark.usefixtures("init_pygame")
def test_move_piece() -> None:
    board = Board()

    first_black_pawn = (1, 0)
    one_space_forward = (2, 0)
    board.move_piece(first_black_pawn, one_space_forward)

    piece_to_evaluate = one_space_forward  # rename only for legibility of intent
    actual: Pawn = board.get_piece(piece_to_evaluate)

    assert actual.lookup_name == Pawn.lookup_name
    assert actual.color == Pawn.BLACK


@patch("pygame.draw.rect")
@pytest.mark.usefixtures("init_pygame")
def test_draw(patched_draw_rect: MagicMock) -> None:
    board = Board()

    rank_and_file_length = 8
    board_length = rank_and_file_length
    surface = pygame.display.set_mode((board_length, board_length))

    first_black_pawn = (1, 0)
    selected = first_black_pawn

    board.draw(surface, selected)

    # 8 ranks * 8 files + Once to render a red border.
    assert patched_draw_rect.call_count == 65

    # Assert that the call to set the border color to board.select_color exists.
    call_exists = any(call.kwargs.get("color") == board.selected_border_color for call in patched_draw_rect.call_args_list)
    assert call_exists


@pytest.mark.usefixtures("init_pygame")
def test_draw_with_scenario() -> None:
    with patch("chess.game.scenario.scenario_factory.ScenarioFactory.get") as patched_scenario_get:
        scenario = "the_setup"
        Board(scenario=scenario)

        call_args_list = patched_scenario_get.call_args_list
        call_exists = any(call.kwargs.get("scenario") == scenario for call in call_args_list)
        assert call_exists
