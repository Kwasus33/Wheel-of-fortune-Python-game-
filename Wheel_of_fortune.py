from Words import Word
import random


class EmptyWheelOfFortuneError(Exception):
    pass


class Wheel_data():
    pass


class Wheel_of_fortune():
    def __init__(self, values: list[(str, "Word")] = None) -> None:
        self._values = values if values else []
        if not values:
            raise EmptyWheelOfFortuneError("Wheel of fortune cannot be empty")

    @property
    def values(self):
        return self._values

    def spin_wheel(self) -> str:
        value = random.choice(self.values)
        return value
