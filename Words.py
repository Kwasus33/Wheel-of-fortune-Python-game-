VOCALS = ['A', 'Ą', 'E', 'Ę', 'I', 'O', 'Ó', 'U']
CONSONANTS = ['B', 'C', 'Ć', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
              'Ł', 'M', 'N', 'Ń', 'P', 'Q', 'R', 'S', 'Ś', 'T',
              'W', 'V', 'X', 'Y', 'Z', 'Ź', 'Ż']


class EmptyWordError(Exception):
    pass


class WordNotGivenError(Exception):
    pass


class Word():
    """
    Class Word atributes:

    param word:
    type word: str

    param category:
    type category: str
    """
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
    def word(self) -> str:
        """
        Returns word attribute of Word object
        """
        return self._word

    @property
    def category(self) -> str:
        """
        Returns category attribute of Word object
        """
        return self._category

    def word_repr(self, letter_guesses: list = None) -> str:
        """
        Returns word representation with exposed guessed letters
        """
        letter_guesses = letter_guesses if letter_guesses else []
        word_repr = ''

        for letter in self._word:
            if letter in letter_guesses or (letter not in CONSONANTS and
                                            letter not in VOCALS):
                word_repr += letter
            else:
                word_repr += '_'

        return word_repr
