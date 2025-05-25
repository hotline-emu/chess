from typing import Any
import pygame
from pygame import Surface
from chess.game.engine import Engine


class Instance:
    """Exists to be used as a disposable. Debatable if worth the effort."""

    def __init__(self, config: dict[str, Any]):
        self.tile_size: int = config.get("tile_size", 80)
        self.scale_multiplier: int = config.get("scale_multiplier", 8)
        self.framerate: int = config.get("framerate", 60)
        self.scenario: str | None = config.get("scenario", None)

        self.engine: Engine | None = None
        self.clock = pygame.time.Clock()
        self.is_running = False

    def __enter__(self) -> "Instance":
        pygame.init()

        board_length = self.tile_size * self.scale_multiplier
        display: Surface = pygame.display.set_mode((board_length, board_length))
        self.engine = Engine(display, self.scenario)
        self.is_running = True

        return self

    def run(self) -> None:
        while self.is_running:
            self.clock.tick(self.framerate)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                self.engine.handle_event(event)

            self.engine.update()
            self.engine.draw()
            pygame.display.flip()

    def __exit__(
        self,
        _exc_type: Any,
        _exc_val: Any,
        _exc_tb: Any,
    ) -> None:
        pygame.quit()
