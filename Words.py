import random


class EmptyWordError(Exception):
    pass


class InvalidLetterValueError(Exception):
    pass


class Words():
    def __init__(self, words: list["Word"] = None) -> None:
        self._words = words if words else []

    @property
    def words(self):
        return self._words

    def random_choice(self):
        return random.choice(self.words)


class Word():
    def __init__(self, word: str) -> None:
        if not word:
            return EmptyWordError('Password cannot be empty')

        self._word = str(word)
        self._letters_list = []

        for letter in self._word:
            if letter != ' ':
                self._letters_list.append(str(letter))

        self._letter_pos = enumerate(self._word)

    @property
    def word(self):
        return self._word

    def letter_representation(self) -> str:
        self._underscape_repr = ''
        for letter in self._word:
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
            for pos, value in self._letter_pos:
                if guess_letter == value and current_letter_repr[pos] == '_':
                    self._new_underscape_repr += guess_letter
                else:
                    self._new_underscape_repr += current_letter_repr[pos]
        else:
            self._new_underscape_repr = str(current_letter_repr)
        return self._new_underscape_repr
