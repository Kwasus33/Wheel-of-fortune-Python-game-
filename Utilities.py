from Words import Word
import csv


class MalformedWheelOfFortuneDataError(Exception):
    pass


def read_from_file_v2(fh):
    words = []
    for line in fh:
        line = line.lstrip()
        line = line.rstrip()
        word = Word(line)
        words.append(word)
    return words


def read_from_file(path):
    words = []
    with open(path, 'r') as file_handle:
        for line in file_handle:
            line = line.lstrip()
            line = line.rstrip()
            word = Word(line)
            words.append(word)
    return words


def read_from_csv(fh):
    list_of_wheel_values = []
    reader = csv.DictReader(fh)
    try:
        for row in reader:
            # if len(row.values()) == 2:
            #     pass
            key = clear_word(row['key'])
            value = clear_word(row['value'])
            list_of_wheel_values.append((key, Word(value)))
    except csv.Error as e:
        raise MalformedWheelOfFortuneDataError(str(e))
    return list_of_wheel_values


def clear_char(letter: str):
    letter = str(letter)
    letter = letter.rstrip().lstrip()
    if len(letter) != 1:
        # try:
        #     letter = int(letter)
        #     return 'Given number is out of range'
        # except TypeError:
        return 'Given character is to long'
    else:
        return letter


def clear_word(current_letter_repr):
    current_letter_repr = str(current_letter_repr).rstrip().lstrip()
    return current_letter_repr
