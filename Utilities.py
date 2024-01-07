from Words import Word
import csv
import json
import os


class MalformedWordDataError(Exception):
    pass


class InvalidWordDataError(Exception):
    def __init__(self, item) -> None:
        super().__init__("Invalid wordlist data detected")
        self.item = item


def read_from_json(fh) -> list["Word"]:
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
        except Exception as e:
            raise InvalidWordDataError(item) from e
    return list_of_words


def read_from_csv(fh) -> list["Word"]:
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


def clear_word(word) -> str:
    """
    Returns cleared of leftside or rightside whitespace char, word or sentance
    """
    word = str(word).strip()
    return word


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
