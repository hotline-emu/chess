from random import choice

HEADS = "heads"
TAILS = "tails"


class Coin:
    SIDES = [
        HEADS,
        TAILS,
    ]

    def __init__(self) -> None:
        self.side: str | None = None

    def flip(self) -> str:
        flipped_result = choice(self.SIDES)
        self.side = flipped_result
        return flipped_result
