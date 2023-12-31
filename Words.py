import random


VOCALS = ['A', 'Ą', 'E', 'Ę', 'I', 'O', 'Ó', 'U']
CONSONANTS = ['B', 'C', 'Ć', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ł', 'M', 'N',
              'Ń', 'P', 'R', 'S', 'Ś', 'T', 'W', 'V', 'X', 'Y', 'Z', 'Ź', 'Ż']


class EmptyWordError(Exception):
    pass


class EmptyWordListError(Exception):
    pass


# class InvalidLetterValueError(Exception):
#     pass


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

    def word_repr(self, letter_guesses: list = None):

        self.letter_guesses = letter_guesses if letter_guesses else []
        word_repr = ''

        for letter in self._word:
            if letter in self.letter_guesses or (letter not in CONSONANTS and
                                                 letter not in VOCALS):
                word_repr += letter
            else:
                word_repr += '_'

        return word_repr
