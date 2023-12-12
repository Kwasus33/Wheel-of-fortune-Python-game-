from Passwords import Password, read_from_file
import random


class Wheel_of_fortune():
    def __init__(self, passwords: list[Password] = None) -> None:
        self._passwords = passwords if passwords else []

    @property
    def passwords(self):
        return self._passwords

    def random_choice(self):
        return random.choice(self.passwords)


wheel = Wheel_of_fortune(read_from_file('passwords.txt'))

print(wheel.random_choice().password)


# password = Password('tuman luk')
# print(password.letter_representation())
# print(password._letters_list)
# print(password.letter_representation('m'))
