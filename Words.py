import random


class EmptyWordError(Exception):
    pass


class EmptyWordListError(Exception):
    pass


class InvalidLetterValueError(Exception):
    pass


class Words():
    def __init__(self, words: list["Word"] = None) -> None:
        """

        """
        self._words = words if words else []
        if not self._words:
            raise EmptyWordListError("List of Words to guess cannot be empty")

    @property
    def words(self):
        """

        """
        return self._words

    def draw_word(self) -> "Word":
        """

        """
        return random.choice(self.words)


class Word():
    def __init__(self, word: str, category: str = None) -> None:
        """

        """
        if not word:
            raise EmptyWordError('Word have to be given')

        self._word = str(word).upper()
        self._category = str(category).upper()
        self._letters_dict = {}

        for letter in self._word:
            if letter != ' ':
                if letter not in self._letters_dict:
                    self._letters_dict[str(letter)] = 1
                else:
                    self._letters_dict[str(letter)] += 1

    @property
    def word(self):
        """

        """
        return self._word

    @property
    def category(self):
        return self._category

    @property
    def letters_dict(self):
        """

        """

        return self._letters_dict

    def letter_repr(self) -> str:
        """

        """
        self._underscape_repr = ''
        for letter in self._word:
            if letter == ' ':
                self._underscape_repr += ' '
            else:
                self._underscape_repr += '_'
        return self._underscape_repr

    def update_letter_repr(self, current_letter_repr: str,
                           guess_letter: str = None) -> str:
        """

        """
        guess_letter = str(guess_letter).upper()
        new_underscape_repr = ''
        if guess_letter is not None:
            for pos, value in enumerate(self._word):
                if guess_letter == value and current_letter_repr[pos] == '_':
                    new_underscape_repr += guess_letter
                else:
                    new_underscape_repr += current_letter_repr[pos]
        else:
            new_underscape_repr = str(current_letter_repr)
        return new_underscape_repr
