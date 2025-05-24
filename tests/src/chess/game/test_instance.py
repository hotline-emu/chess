from unittest.mock import patch, MagicMock
import pytest
import pygame
from chess.game.instance import Instance


@pytest.fixture
def test_config():
    return {
        "tile_size": 64,
        "scale_multiplier": 10,
        "framerate": 30,
    }


def test_disposable(test_config):
    with patch("pygame.init") as patched_init:
        with patch("pygame.display.set_mode") as patched_set_mode:
            with patch(
                "chess.game.instance.Engine",
            ) as patched_engine:
                display_mock = MagicMock()
                patched_set_mode.return_value = display_mock

                with Instance(test_config) as instance:
                    tile_size = test_config.get("tile_size")
                    scale_multiplier = test_config.get("scale_multiplier")
                    board_length = tile_size * scale_multiplier
                    size = (  # This is the asserted parameter name from the signature.
                        board_length,
                        board_length,
                    )

                    patched_init.assert_called_once()
                    patched_set_mode.assert_called_once_with(size)
                    patched_engine.assert_called_once_with(display_mock)
                    assert instance.game is patched_engine.return_value
                    assert instance.is_running is True


def test_disposable_exits(test_config):
    with patch("pygame.quit") as patched_quit:
        instance = Instance(test_config)
        instance.__exit__(None, None, None)
        patched_quit.assert_called_once()


def test_run_processes_events_and_calls_engine(test_config):
    with patch("pygame.display.set_mode", return_value=MagicMock()):
        with patch("pygame.event.get") as patched_event_get:
            with patch("pygame.display.flip") as patched_display_flip:
                with patch("pygame.time.Clock") as patched_clock:
                    with patch("chess.game.instance.Engine") as patched_engine:
                        mock_event = pygame.event.Event(pygame.QUIT)
                        patched_event_get.return_value = [mock_event]
                        engine_mock = MagicMock()
                        patched_engine.return_value = engine_mock

                        with Instance(test_config) as instance:
                            instance.run()

                        patched_clock.return_value.tick.assert_called_once_with(
                            test_config["framerate"]
                        )
                        engine_mock.handle_event.assert_called_once_with(mock_event)
                        engine_mock.update.assert_called_once()
                        engine_mock.draw.assert_called_once()
                        patched_display_flip.assert_called_once()
                        assert instance.is_running is False
