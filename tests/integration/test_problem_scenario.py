import logging
import pytest
from chess.game.instance import Instance
from chess.components.pieces import AbstractPiece, Rook, Bishop
from tests.integration.utilities import Coin, Die
from tests.integration.utilities.coin import HEADS
from tests.integration.utilities.game_helpers import (
    render_board,
    decipher_location_to_chess_coordinates,
)
from environs import Env

env = Env()
env.read_env()

logger = logging.getLogger(__name__)

SLOW_DOWN = env.bool("slow_down")
ROOK_IS_ALLOWED_TO_WIN_BY_EXECUTION = env.bool("rook_is_allowed_to_win_by_execution")


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
    coin = Coin()
    die_a = Die()
    die_b = Die()

    rook_initial_location = (7, 7)  # The rook starts here per the scenario terms.
    rook_current_location = rook_initial_location

    bishop_terminal_location = (5, 2)  # The bishop does not move.
    bishop_actual: Bishop = instance.engine.board.get_piece(bishop_terminal_location)

    rook_can_be_executed = False
    turns = 15
    for turn_index in range(turns):
        nth_turn = turn_index + 1  # Increment so that the log doesn't start from zero.
        logger.info("Turn %s.", nth_turn)
        render_board(instance, SLOW_DOWN)

        face, dice_value = __get_coin_and_dice_values(coin, die_a, die_b)

        rook_destination_location = __get_rook_desination_location(
            face,
            dice_value,
            rook_current_location,
        )

        ensure_rook_is_present_at_coordinate(instance, rook_current_location)

        # There is nothing in the scenario indicating what to do if the rook takes the bishop.
        rook_destination_is_bishop_location = rook_destination_location == bishop_terminal_location
        if rook_destination_is_bishop_location:
            # Program two possible outcomes for this case.
            if ROOK_IS_ALLOWED_TO_WIN_BY_EXECUTION:
                logger.info("The rook has moved into a position where it will execute the bishop.")
                break
            else:
                # Re-flip coin and re-roll dice.
                logger.info("The rook would execute the bishop under these conditions, re-rolling turn.")
                rook_destination_location = reroll_for_new_destination(
                    rook_destination_is_bishop_location,
                    coin,
                    die_a,
                    die_b,
                    rook_current_location,
                    bishop_terminal_location,
                )

        move_piece_and_render_board(instance, rook_current_location, rook_destination_location)
        rook_current_location = rook_destination_location

        rook_can_be_executed = __can_rook_be_executed(
            bishop_actual,
            bishop_terminal_location,
            rook_current_location,
        )
        if rook_can_be_executed:
            break

    winner = "bishop" if rook_can_be_executed else "rook"
    logger.info("The %s has won.", winner)


def __get_coin_and_dice_values(coin: Coin, die_a: Die, die_b: Die) -> tuple[str, int]:
    face = coin.flip()
    value_a = die_a.roll()
    value_b = die_b.roll()
    dice_value = value_a + value_b
    logger.info("Coin: %s | Dice: %s (%s + %s)", face, dice_value, value_a, value_b)

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
        logger.debug("The rook is moving right %s spaces.", dice_value)
        # rook moves up <dice_value> spaces
        # if rook exceeds the board top, they show back up on the bottom.
        # rightmost space is index 7 -> back to 0
        rightmost_file_index = 7
        target_file_index = current_file + dice_value
        while target_file_index > rightmost_file_index:
            logger.debug("The rook went off the board, moving to the first file.")
            target_file_index -= 8

        destination_rank = current_rank
        destination_file = target_file_index
        destination_location = (destination_rank, destination_file)
        logger.info(
            "The rook is moving from %s to %s.",
            decipher_location_to_chess_coordinates(current_location),
            decipher_location_to_chess_coordinates(destination_location),
        )

        return destination_location

    # Face must logically be tails here.
    logger.debug("The rook is moving up %s spaces.", dice_value)
    # rook moves right <dice_value> spaces
    # if rook exceeds the right edge, they show back up on the left edge.
    # topmost space is index 0 -> back to 7
    topmost_rank_index = 0
    target_rank_index = current_rank - dice_value
    while target_rank_index < topmost_rank_index:
        logger.debug("The rook went off the board, moving to the first rank.")
        target_rank_index += 8

    destination_rank = target_rank_index
    destination_file = current_file
    destination_location = (destination_rank, destination_file)
    logger.info(
        "The rook is moving from %s to %s.",
        decipher_location_to_chess_coordinates(current_location),
        decipher_location_to_chess_coordinates(destination_location),
    )
    return destination_location


def __can_rook_be_executed(
    bishop: Bishop,
    bishop_location: tuple[int, int],
    rook_location: tuple[int, int],
) -> bool:
    execution_is_possible = bishop.is_legal_move(bishop_location, rook_location)

    if execution_is_possible:
        logger.info("The rook has moved into a position where the bishop can legally execute it.")

    return execution_is_possible


def ensure_rook_is_present_at_coordinate(instance: Instance, coordinate: tuple[int, int]):
    rook_instance: AbstractPiece = instance.engine.board.get_piece(coordinate)
    if not isinstance(rook_instance, Rook):
        message = "Bug detected with Rook movement logic. See logs."
        logger.error(message)
        raise Exception(message)


def move_piece_and_render_board(
    instance: Instance,
    rook_current_location: tuple[int, int],
    rook_destination_location: tuple[int, int],
):
    destination_is_not_the_current_space = rook_current_location != rook_destination_location
    if destination_is_not_the_current_space:
        instance.engine.board.move_piece(
            rook_current_location,
            rook_destination_location,
        )
    render_board(instance)


def reroll_for_new_destination(
    rook_destination_is_bishop_location: bool,
    coin: Coin,
    die_a: Die,
    die_b: Die,
    rook_current_location: tuple[int, int],
    bishop_terminal_location: tuple[int, int],
):
    rerolled_rook_destination_location = None
    while rook_destination_is_bishop_location:
        face, dice_value = __get_coin_and_dice_values(coin, die_a, die_b)
        rerolled_rook_destination_location = __get_rook_desination_location(
            face,
            dice_value,
            rook_current_location,
        )
        rook_destination_is_bishop_location = rerolled_rook_destination_location == bishop_terminal_location
        if rook_destination_is_bishop_location:
            logger.info("The rook would still execute the bishop under these conditions, re-rolling turn.")

    return rerolled_rook_destination_location
