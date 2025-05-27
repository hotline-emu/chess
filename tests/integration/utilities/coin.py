from random import choice

HEADS = "heads"
TAILS = "tails"


class Coin:
    SIDES = [
        HEADS,
        TAILS,
    ]

    def flip(self) -> str:
        return choice(self.SIDES)
