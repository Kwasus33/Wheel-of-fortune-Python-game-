from Words import Word
from Utilities import clear_char
import random


class EmptyWheelOfFortuneError(Exception):
    pass


class Wheel_data():
    pass


class Wheel_of_fortune():
    def __init__(self, values: list["Word"] = None) -> None:
        self._values = values if values else []
        if not values:
            raise EmptyWheelOfFortuneError("Wheel of fortune cannot be empty")

    @property
    def values(self):
        return self._values

    def random_choice(self) -> str:
        value = random.choice(self.values)
        cleared_value = clear_char(str(value.word))
        return cleared_value
