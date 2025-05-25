from random import choice

HEADS = "heads"
TAILS = "tails"


class Coin:
    SIDES = [
        HEADS,
        TAILS,
    ]

    def __init__(self) -> None:
        self.side = None

    def flip(self) -> str:
        self.side = choice(self.SIDES)
        return self.side
