from Words import Word
import csv


class MalformedWheelOfFortuneDataError(Exception):
    pass


def read_from_json(fh):
    pass


def read_from_csv(fh):
    """
    Return a list of class Word objects read from file
    """
    list_of_values = []
    reader = csv.DictReader(fh)
    try:
        for row in reader:
            if 'key' in row.keys():
                key = clear_word(row['key'])
            else:
                key = None
            value = clear_word(row['value'])
            list_of_values.append(Word(value, key))
    except csv.Error as e:
        raise MalformedWheelOfFortuneDataError(str(e))
    return list_of_values


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


def choose_game_mode():
    pass
