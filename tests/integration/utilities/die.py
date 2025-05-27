from random import randint


class Die:
    def __init__(self, number_of_sides: int = 6) -> None:
        self.number_of_sides = number_of_sides

    def roll(self) -> int:
        return randint(1, self.number_of_sides)
