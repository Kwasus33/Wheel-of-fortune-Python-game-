from Words import Word, read_from_file
from Utilities import clear_char
import random


class Wheel_of_fortune():
    def __init__(self, words: list[Word] = None) -> None:
        self._words = words if words else []

    @property
    def words(self):
        return self._words

    def random_choice(self):
        return random.choice(self.words)


wheel = Wheel_of_fortune(read_from_file('words.txt'))
drawn_word = wheel.random_choice()
current_letter_repr = str(drawn_word.letter_representation())

while True:
    print(current_letter_repr)
    print(drawn_word.word)
    letter = input(str())
    cleared_letter = clear_char(letter)
    print(cleared_letter)
    info = drawn_word.update_letter_representation(current_letter_repr,
                                                   cleared_letter)
    print(info)
    current_letter_repr = str(info)


# password = Password('tuman luk')
# print(password.letter_representation())
# print(password._letters_list)
# print(password.letter_representation('m'))
