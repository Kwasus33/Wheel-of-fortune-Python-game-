class EmptyPasswordError(Exception):
    pass


class InvalidLetterValueError(Exception):
    pass


class Password():
    def __init__(self, password: str) -> None:
        if not password:
            return EmptyPasswordError('Password cannot be empty')

        self._password = str(password)
        self._letters_list = []

        for letter in self._password:
            if letter != ' ':
                self._letters_list.append(str(letter))

        self._letter_pos = enumerate(self._password)

    @property
    def password(self):
        return self._password

    def letter_representation(self) -> str:
        self._underscape_repr = ''
        for letter in self._password:
            if letter == ' ':
                self._underscape_repr += ' '
            else:
                self._underscape_repr += '_'
        return self._underscape_repr

    def update_letter_representation(self, current_letter_repr: str,
                                     guess_letter: str = None) -> str:
        guess_letter = str(guess_letter)
        self._new_underscape_repr = ''
        if guess_letter is not None:
            for letter_p, letter__ in self._password, current_letter_repr:
                # i have to make a list of tuples consinting of
                # next letters of self._password and current_letter_repr
                if letter_p == guess_letter and letter__ == '_':
                    self._new_underscape_repr += guess_letter
                else:
                    self._new_underscape_repr += letter__
        else:
            self._new_underscape_repr = str(self.letter_representation())
        return self._new_underscape_repr


def read_from_file(path):
    passwords = []
    with open(path, 'r') as file_handle:
        for line in file_handle:
            line = line.lstrip()
            line = line.rstrip()
            password = Password(line)
            passwords.append(password)
    return passwords
