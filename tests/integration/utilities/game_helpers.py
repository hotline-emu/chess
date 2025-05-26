import time
import pygame
from chess.game.instance import Instance

RANK_MAP = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

FILE_MAP = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}


def render_board(instance: Instance, slow_down: bool = False) -> None:
    instance.engine.update()
    instance.engine.draw()
    pygame.display.flip()

    if slow_down:
        one_second = 1
        time.sleep(one_second)


def decipher_location_to_chess_coordinates(
    location: tuple[int, int],
) -> str:
    rank, file = location
    translated_rank = RANK_MAP.get(rank)
    translated_file = FILE_MAP.get(file)

    return f"{translated_rank}{translated_file}"
