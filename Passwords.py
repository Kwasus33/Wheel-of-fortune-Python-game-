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

    def letter_representation(self, guess_letter: str = None) -> str:
        self._underscape_repr = ''
        guess_letter = str(guess_letter)
        if guess_letter is not None:
            for letter in self._password:
                if letter == ' ':
                    self._underscape_repr += ' '
                else:
                    if letter == guess_letter:
                        self._underscape_repr += f'{guess_letter}'
                    else:
                        self._underscape_repr += '_'
        else:
            for letter in self._password:
                if letter == ' ':
                    self._underscape_repr += ' '
                else:
                    self._underscape_repr += '_'
        return self._underscape_repr


def read_from_file(path):
    passwords = []
    with open(path, 'r') as file_handle:
        for line in file_handle:
            line = line.lstrip()
            line = line.rstrip()
            password = Password(line)
            passwords.append(password)
    return passwords
