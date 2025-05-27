# MyPy will complain about get() from the config.
# In the case of the test, the received variable is controlled by the test. Overzealous type checking is unnecessary.
# mypy: disable-error-code=assignment

from unittest.mock import patch, MagicMock
import pytest
import pygame
from chess.game.instance import Instance


@pytest.fixture
def test_config() -> dict[str, int]:
    return {
        "tile_size": 64,
        "scale_multiplier": 10,
        "framerate": 30,
    }


@patch(
    "chess.game.instance.Engine",
)
@patch("pygame.display.set_mode")
@patch("pygame.init")
def test_disposable(
    patched_init: MagicMock,
    patched_set_mode: MagicMock,
    patched_engine: MagicMock,
    test_config: dict[str, int],
) -> None:
    display_mock = MagicMock()
    patched_set_mode.return_value = display_mock

    with Instance(test_config) as instance:
        tile_size: int = test_config.get("tile_size")
        scale_multiplier: int = test_config.get("scale_multiplier")
        board_length = tile_size * scale_multiplier
        size = (  # This is the asserted parameter name from the signature.
            board_length,
            board_length,
        )

        patched_init.assert_called_once()
        patched_set_mode.assert_called_once_with(size)
        patched_engine.assert_called_once_with(display_mock, None)
        assert instance.engine is patched_engine.return_value
        assert instance.is_running is True


@patch("pygame.quit")
def test_disposable_exits(
    patched_quit: MagicMock,
    test_config: dict[str, int],
) -> None:
    instance = Instance(test_config)
    instance.__exit__(None, None, None)
    patched_quit.assert_called_once()


@patch("chess.game.instance.Engine")
@patch("pygame.time.Clock")
@patch("pygame.display.flip")
@patch("pygame.event.get")
@patch("pygame.display.set_mode", return_value=MagicMock())
def test_run_processes_events_and_calls_engine(
    _display_set_mode: MagicMock,
    patched_event_get: MagicMock,
    patched_display_flip: MagicMock,
    patched_clock: MagicMock,
    patched_engine: MagicMock,
    test_config: dict[str, int],
) -> None:
    mock_event = pygame.event.Event(pygame.QUIT)
    patched_event_get.return_value = [mock_event]
    engine_mock = MagicMock()
    patched_engine.return_value = engine_mock

    with Instance(test_config) as instance:
        instance.run()

    patched_clock.return_value.tick.assert_called_once_with(test_config["framerate"])
    engine_mock.handle_event.assert_called_once_with(mock_event)
    engine_mock.update.assert_called_once()
    engine_mock.draw.assert_called_once()
    patched_display_flip.assert_called_once()
    assert instance.is_running is False
