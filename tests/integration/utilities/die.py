from random import randint


class Die:
    def __init__(self, number_of_sides=6) -> None:
        self.number_of_sides = number_of_sides
        self.value = None

    def roll(self) -> int:
        self.value = randint(1, self.number_of_sides)
        return self.value
