import logging
import pytest
import pygame
import time
from chess.game.instance import Instance
from tests.integration.utilities import Coin, Die
from tests.integration.utilities.coin import HEADS
from environs import Env

env = Env()
env.read_env()

logger = logging.getLogger(__name__)


@pytest.fixture
def instance():
    config = {
        "tile_size": env.int("tile_size"),
        "framerate": env.int("framerate"),
        "scale_multiplier": env.int("scale_multiplier"),
        "scenario": "the_problem",
    }

    # Instead of using instance as a disposable...
    # Manually call the disposable bits in the fixture setup and teardown.
    instance = Instance(config)
    instance.__enter__()
    yield instance
    instance.__exit__(None, None, None)


def test_the_problem(instance) -> None:
    slow_down = env.bool("slow_down")

    coin = Coin()
    die_a = Die()
    die_b = Die()

    rook_initial_location = (7, 7)  # The bishop starts here per the scenario terms.
    bishop_terminal_location = (5, 2)  # The bishop does not move.
    rook_current_location = rook_initial_location

    rook_has_been_executed = False

    turns = 15
    for turn_index in range(turns):
        nth_turn = turn_index + 1
        logger.info("turn %s", nth_turn)
        __render_board(instance, slow_down)

        face, dice_value = __get_coin_and_dice_values(coin, die_a, die_b)

        rook_destination_location = __get_rook_desination_location(
            face,
            dice_value,
            rook_current_location,
        )

        logger.info(
            "rook moving from %s to %s",
            rook_current_location,
            rook_destination_location,
        )

        #! TODO: Trigger board move.
        rook_current_location = rook_destination_location

        rook_has_been_executed = __can_rook_be_executed(
            rook_current_location,
            bishop_terminal_location,
        )
        if rook_has_been_executed:
            break

    winner = "bishop" if rook_has_been_executed else "rook"
    logger.info("The %s has won", winner)


def __get_coin_and_dice_values(coin: Coin, die_a: Die, die_b: Die) -> tuple[str, int]:
    face = coin.flip()
    logger.info("coin flip resulted in %s", face)
    value_a = die_a.roll()
    value_b = die_b.roll()
    dice_value = value_a + value_b
    logger.info(
        "dice total %s (from %s and %s)",
        dice_value,
        value_a,
        value_b,
    )

    return (
        face,
        dice_value,
    )


def __get_rook_desination_location(
    face: str,
    dice_value: int,
    current_location: tuple[int, int],
) -> tuple[int, int]:
    current_rank, current_file = current_location

    if face == HEADS:
        logger.info("the rook is moving right %s spaces", dice_value)
        # rook moves up <dice_value> spaces
        # if rook exceeds the board top, they show back up on the bottom.
        # rightmost space is index 7 -> back to 0
        rightmost_file_index = 7
        target_file_index = current_file + dice_value
        while target_file_index > rightmost_file_index:
            logger.info("rook went off the board, moving to the first file")
            target_file_index -= 8

        destination_rank = current_rank
        destination_file = target_file_index
        return (
            destination_rank,
            destination_file,
        )

    # Face must logically be tails here.
    logger.info("the rook is moving up %s spaces", dice_value)
    # rook moves right <dice_value> spaces
    # if rook exceeds the right edge, they show back up on the left edge.
    # topmost space is index 0 -> back to 7
    topmost_rank_index = 0
    target_rank_index = current_rank - dice_value
    while target_rank_index < topmost_rank_index:
        logger.info("rook went off the board, moving to the first rank")
        target_rank_index += 8

    destination_rank = target_rank_index
    destination_file = current_file
    return (
        destination_rank,
        destination_file,
    )


def __can_rook_be_executed(rook_current_location, bishop_current_location) -> bool:
    return False


def __render_board(instance: Instance, slow_down=False) -> None:
    instance.engine.update()
    instance.engine.draw()
    pygame.display.flip()

    if slow_down:
        one_second = 1
        time.sleep(one_second)
