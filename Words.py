import random


VOCALS = ['A', 'Ą', 'E', 'Ę', 'I', 'O', 'Ó', 'U', 'Y']
CONSONANTS = ['B', 'C', 'Ć', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ł', 'M', 'N',
              'Ń', 'P', 'R', 'S', 'Ś', 'T', 'W', 'V', 'X', 'Y', 'Z', 'Ź', 'Ż']


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

    @property
    def word(self):
        """

        """
        return self._word

    @property
    def category(self):
        return self._category

    def letter_repr(self) -> str:
        """

        """
        self._underscape_repr = ''
        for letter in self._word:
            if letter not in CONSONANTS and letter not in VOCALS:
                self._underscape_repr += letter
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
