from Words import Word
import csv


class MalformedWheelOfFortuneDataError(Exception):
    pass


def read_from_file(path):
    words = []
    with open(path, 'r') as file_handle:
        for line in file_handle:
            line = line.lstrip()
            line = line.rstrip()
            word = Word(line)
            words.append(word)
    return words


def read_from_csv(path):
    list_of_wheel_values = []
    with open(path, 'r') as fh:
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
        return 'Given letter is to long'
    else:
        return letter


def clear_word(current_letter_repr):
    current_letter_repr = str(current_letter_repr).rstrip().lstrip()
    return current_letter_repr


# """Już działa read_from_csv"""
# list = read_from_csv('values.txt')
# for obj in list:
#     print(len(obj))
