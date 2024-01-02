from Words import Word
import random


class EmptyWheelOfFortuneError(Exception):
    pass


class Wheel_data():
    pass


class Wheel_of_fortune():
    """
    Class Wheel of fortune contains attributes:

    param values: list of values that can be drawn in a wheel spin
    type values: list of class Word objects
    """
    def __init__(self, values: list["Word"] = None) -> None:
        """
        Creates instance of Wheel of fortune
        Raises EmptyWheelOfFortuneError if empty list of values is given
        """
        self._values = values if values else []
        if not values:
            raise EmptyWheelOfFortuneError("Wheel of fortune cannot be empty")

    @property
    def values(self):
        """
        Returns list of wheel values
        """
        return self._values

    def spin_wheel(self) -> "Word":
        """
        Spins a wheel and returns a drawn value
        """
        return random.choice(self.values)
