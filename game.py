from Words import Words, Word
from Wheel_of_fortune import Wheel_of_fortune
from Utilities import read_from_file, read_from_csv, clear_word, clear_char


class Player():
    def __init__(self, idx: int = None, balance: int = 0) -> None:
        self._id = idx
        self._balance = balance

    @property
    def id(self):
        return self._id

    def balance(self):
        return self._balance

    def set_balance(self, amount):
        self._balance += amount


class GameMenu():
    def __init__(self, path: str, num_of_players: int = 0) -> None:
        self._players_num = num_of_players
        self._path = path
        self._words = Words(read_from_file(self._path))
        self._wheel = Wheel_of_fortune(read_from_csv('values.txt'))

    @property
    def get_players(self) -> list:
        players = []
        for idx in range(self._players_num):
            players.append(Player(idx+1))
        return players

    def game_items(self) -> (Words, Wheel_of_fortune):
        return (self._words, self._wheel)


class GameRound():
    def __init__(self, players: list["Player"], word: Word) -> None:
        self._players = players
        self._word = word

    @property
    def players(self):
        return self._players

    def play(self):

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


class Final():
    pass


