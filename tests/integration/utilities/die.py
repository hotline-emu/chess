from random import randint


class Die:
    def __init__(self, number_of_sides: int = 6) -> None:
        self.number_of_sides = number_of_sides
        self.value: int | None = None

    def roll(self) -> int:
        rolled_value = randint(1, self.number_of_sides)
        self.value = rolled_value
        return rolled_value
