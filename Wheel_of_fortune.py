class EmptyPasswordError(Exception):
    pass


class InvalidLetterValueError(Exception):
    pass


class Password():
    def __init__(self, password: str) -> None:
        password = str(password)

        if not password:
            return EmptyPasswordError('Password cannot be empty')

        password = password.lstrip()
        password = password.rstrip()
        self._password = password
        self._letters_list = []

        for letter in self._password:
            if letter != ' ':
                self._letters_list.append(str(letter))

        self._letter_pos = enumerate(self._password)

    @property
    def password(self):
        return self._password

    def letter_representation(self):
        self._underscape_repr = ''
        for letter in self._password:
            if letter == ' ':
                self._underscape_repr += ' '
            else:
                self._underscape_repr += '_'
        return self._underscape_repr

    # def guess_letter(self):
    #     self._current_letters_guess = ''
    #     for letter in self._password:
    #         if letter == self._password[-1]:
    #             if letter in self._letters_list:
    #                 self._current_letters_guess += str(letter)
    #             else:
    #                 self._current_letters_guess += '_'
    #         else:
    #             if letter in self._letters_list:
    #                 self._current_letters_guess += f'{str(letter)} '
    #             else:
    #                 self._current_letters_guess += '_ '

    def insert_guessed_letter(self, guess_letter):
        guess_letter = str(guess_letter)

        if not guess_letter:
            raise InvalidLetterValueError('Invalid letter value was given')
        if guess_letter in self._letters_list:
            for pos, value in self._letter_pos:
                if str(guess_letter) == value:
                    to_replace = self._underscape_repr[pos]
                    self._underscape_repr.replace(to_replace, guess_letter)
            self._letters_list.remove(guess_letter)
        return self._underscape_repr

        # gdyby nie usuwanie litery ze słownika liter
        # i sprawdzania jej obecności w pierwszym if, byłaby sytuacja:
        # jeżeli litera występuje wielokrotnie
        # to za pierwszym razem ją podmienia
        # a potem przy następnych obrotach,
        # gdy ją napotka, powtarza podmianę
        # jest to nieefektywne, zajmuje pamięć
        # i niepotrzebnie zwiększa złożoność


password = Password('tuman luk')
print(password.letter_representation())
print(password._letters_list)
print(password.insert_guessed_letter('m'))
