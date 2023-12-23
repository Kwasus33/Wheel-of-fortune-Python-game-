from Words import Word, Words
from Wheel_of_fortune import Wheel_of_fortune
from Utilities import read_from_file, read_from_csv, clear_char


class Round():
    def __init__(self) -> None:
        pass


class Final():
    pass


path = 'words.txt'
words = Words(read_from_file(path))

drawn_word = words.random_choice()
letters_in_word = drawn_word.letters_set
word_repr = drawn_word.letter_representation()
wheel = Wheel_of_fortune(read_from_csv('values.txt'))
# for word in words.words:
#     print(word.word)

players_balance = 0

while letters_in_word:
    print(word_repr)
    key, value = wheel.random_choice()
    # value is instance of word class
    if key == 'money':
        print(int(value.word))
        letter = input(str())
        letter = clear_char(letter)
        if letter in letters_in_word:
            letters_in_word.remove(letter)
            players_balance += int(value.word)
            # trzeba przemnożyć przez ilość wystąpień litery odgadniętej
            word_repr = drawn_word.update_letter_repr(word_repr, letter)
    elif value.word == 'BANKRUPT':
        print(value.word)
        players_balance = 0
    elif value.word == 'NAGRODA':
        print(value.word)
        pass
        # losowanie nazwy nagrody z pliku i dodawanie do listy nagród gracza
    elif value.word == 'STOP':
        print(value.word)
        pass
        # gracz traci kolejkę


print(word_repr)
print(players_balance)
