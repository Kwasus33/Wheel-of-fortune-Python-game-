from Words import Word
import csv
import json


class MalformedWordDataError(Exception):
    pass


class InvalidWordDataError(Exception):
    def __init__(self, item) -> None:
        super().__init__("Invalid person data detected")
        self.item = item


def read_from_json(fh):
    """
    Return a list of class Word objects read from .json file
    """
    list_of_words = []
    data = json.load(fh)
    for item in data:
        try:
            if 'key' in item.keys():
                key = clear_word(item['key'])
            else:
                key = None
            value = clear_word(item['value'])
            list_of_words.append(Word(value, key))
            word = Word(value, key)
        except KeyError as e:
            raise MalformedWordDataError('Missing key in file') from e
        except Exception as e:
            raise InvalidWordDataError(item) from e
        list_of_words.append(word)
    return list_of_words


def read_from_csv(fh):
    """
    Return a list of class Word objects read from csv file
    """
    list_of_words = []
    reader = csv.DictReader(fh)
    try:
        for row in reader:
            if 'key' in row.keys():
                key = clear_word(row['key'])
            else:
                key = None
            value = clear_word(row['value'])
            list_of_words.append(Word(value, key))
    except csv.Error as e:
        raise MalformedWordDataError(str(e))
    except Exception as e:
        raise InvalidWordDataError(row) from e
    return list_of_words


def clear_char(letter: str):
    """
    Returns char as a cleared of whitespace string
    """
    letter = str(letter)
    letter = letter.rstrip().lstrip()
    if len(letter) != 1:
        return 'Given character is to long'
    else:
        return letter


def clear_word(word):
    """
    Returns cleared of leftside or rightside whitespace word or sentance
    """
    word = str(word).rstrip().lstrip()
    return word
