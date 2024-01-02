import random


VOCALS = ['A', 'Ą', 'E', 'Ę', 'I', 'O', 'Ó', 'U']
CONSONANTS = ['B', 'C', 'Ć', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
              'Ł', 'M', 'N', 'Ń', 'P', 'Q', 'R', 'S', 'Ś', 'T',
              'W', 'V', 'X', 'Y', 'Z', 'Ź', 'Ż']


class EmptyWordError(Exception):
    pass


class WordNotGivenError(Exception):
    pass


class EmptyWordListError(Exception):
    pass


# class InvalidLetterValueError(Exception):
#     pass


class Words():
    """
    Class Words contains atributes:

    param words: list of class Word objects
    """
    def __init__(self, words: list["Word"] = None) -> None:
        """
        Creates instance of Words
        Raises EmptyWordListError when list is empty
        """
        self._words = words if words else []
        if not self._words:
            raise EmptyWordListError("List of Words to guess cannot be empty")

    @property
    def words(self):
        """
        Returns list of words
        """
        return self._words

    def draw_word(self) -> "Word":
        """
        Draws and returns a word
        """
        return random.choice(self.words)


class Word():
    def __init__(self, word: str = None, category: str = None) -> None:
        """
        Creates instance of Word
        Raises EmptyWordError if word is an empty str
        Raises WordNotGivenError if word is not given
        """
        if word is None:
            raise WordNotGivenError('The word have to be given')

        if not word:
            raise EmptyWordError('Word have to be given')

        self._word = str(word).upper()
        self._category = str(category).upper() if category else 'NO CATEGORY'

    @property
    def word(self):
        """
        Returns word attribute of Word object
        """
        return self._word

    @property
    def category(self):
        """
        Returns category attribute of Word object
        """
        return self._category

    def word_repr(self, letter_guesses: list = None):
        """
        Returns word representation with exposed guessed letters
        """
        self.letter_guesses = letter_guesses if letter_guesses else []
        word_repr = ''

        for letter in self._word:
            if letter in self.letter_guesses or (letter not in CONSONANTS and
                                                 letter not in VOCALS):
                word_repr += letter
            else:
                word_repr += '_'

        return word_repr
