from Words import Words, Word
from Utilities import clear_char, clear_letter_repr, read_from_file
import random


class Wheel_of_fortune():
    def __init__(self, values: list["Word"] = None) -> None:
        self._values = values if values else []

    @property
    def values(self):
        return self._values

    def random_choice(self) -> str:
        value = random.choice(self.values)
        cleared_value = clear_char(str(value.word))
        return cleared_value


wheel = Wheel_of_fortune(read_from_file('values.txt'))
drawn_word = Words(read_from_file('words.txt')).random_choice()
drawn_value = wheel.random_choice()
current_letter_repr = str(drawn_word.letter_representation())


print(drawn_value)
print(drawn_word.word)
print(current_letter_repr)
up = drawn_word.update_letter_representation(current_letter_repr, drawn_value)
print(up)

current_letter_repr = clear_letter_repr(up)
wheel = Wheel_of_fortune(read_from_file('values.txt'))
drawn_value = wheel.random_choice()
print(drawn_value)
print(drawn_word.word)
print(current_letter_repr)
up = drawn_word.update_letter_representation(current_letter_repr, drawn_value)
print(up)

# while True:
#     print(current_letter_repr)
#     print(drawn_word.word)
#     letter = input(str())
#     cleared_letter = clear_char(letter)
#     print(cleared_letter)
#     current_letter_repr = clear_letter_repr(current_letter_repr)
#     info = drawn_word.update_letter_representation(current_letter_repr,
#                                                    cleared_letter)
#     current_letter_repr = str(info)


# password = Password('tuman luk')
# print(password.letter_representation())
# print(password._letters_list)
# print(password.letter_representation('m'))
