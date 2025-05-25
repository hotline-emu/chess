import logging
import pytest
import pygame
from chess.game.engine import Engine
from tests.integration.utilities import Coin, Die

logger = logging.getLogger(__name__)


@pytest.fixture
def engine() -> Engine:
    rank_and_file_count = 8
    board_length = rank_and_file_count
    surface = pygame.display.set_mode((board_length, board_length))
    scenario = "the_problem"

    return Engine(surface, scenario)


@pytest.mark.usefixtures("init_pygame")
def test_the_problem(engine: Engine) -> None:
    coin = Coin()
    die_a = Die()
    die_b = Die()

    face = coin.flip()
    logger.info(face)
    value_a = die_a.roll()
    value_b = die_b.roll()
    dice_value = value_a + value_b
    logger.info(dice_value)
