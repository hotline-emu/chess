from unittest.mock import patch, MagicMock
import pytest
import pygame
from chess.game.engine import Engine
from chess.components.pieces import AbstractPiece


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
            assert engine.selected_position == (
                rank_mouse_position,
                file_mouse_position,
            )


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


@pytest.mark.usefixtures("init_pygame")
@patch("pygame.mouse.get_pos")
@patch("pygame.display.update")
@patch("pygame.time.wait")
def test_handle_event_triggers_illegal_move_message(
    mock_wait: MagicMock,
    mock_update: MagicMock,
    mock_get_pos: MagicMock,
    engine: Engine,
) -> None:
    intended_target_position = (2, 2)
    initial_position = (1, 1)

    # Simulates a click event.
    tile_size = engine.board.tile_size
    mock_get_pos.return_value = (
        intended_target_position[1] * tile_size,
        intended_target_position[0] * tile_size,
    )

    mocked_piece = MagicMock(spec=AbstractPiece)
    mocked_piece.is_legal_move.return_value = False

    engine.board.get_piece = MagicMock(side_effect=lambda position: (mocked_piece if position == initial_position else None))

    # Force the engine to believe that a piece was selected already.
    engine.selected_position = initial_position

    # Trigger the event.
    event = pygame.event.Event(pygame.MOUSEBUTTONDOWN)
    engine.handle_event(event)

    mock_update.assert_called_once()
    mock_wait.assert_called_once_with(1000)
    mocked_piece.is_legal_move.assert_called_once_with(initial_position, intended_target_position)

    # Ensure that the selected piece was deselected.
    assert engine.selected_position is None
