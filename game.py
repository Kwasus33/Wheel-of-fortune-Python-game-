from Words import Words, Word
from Wheel_of_fortune import Wheel_of_fortune
from Utilities import read_from_file, clear_word, clear_char
from database import Database

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
        self._wheel = Wheel_of_fortune(Database().load_from_file('values.txt'))

    @property
    def get_players(self) -> list:
        players = []
        for idx in range(self._players_num):
            players.append(Player(idx+1))
        return players

    def game_items(self) -> (Words, Wheel_of_fortune):
        return (self._words, self._wheel)


class GameRound(GameMenu):
    def __init__(self, players: list["Player"], word: Word) -> None:
        self._players = players
        self._word = word
        # super.__init__(self._words, self._wheel)

    @property
    def players(self):
        return self._players

    def buy_vocal(self):
        print("Press T if u want to buy a vocal, else any other button")
        answer = input(str())
        if clear_char(answer) == 't' or clear_char(answer) == 'T':
            letter = clear_char(input(str()))
            return letter
        return

    def play(self):
        letters_in_word = self._word.letters_set
        word_repr = self._word.letter_repr
        print(self._word.letter_repr)

        while letters_in_word:
            key, value = self._wheel.random_choice()
            # value is instance of word class
            if key == 'money':
                print(int(value.word))
                if self.buy_vocal():
                    letter = self.buy_vocal
                else:
                    letter = input(str())
                    letter = clear_char(letter)
                if letter in letters_in_word:
                    word_repr = self._word.update_letter_repr(word_repr, letter)
                    letters_in_word.remove(letter)
                    players_balance += letter_quantity*int(value.word)
                    # musze zadeklarować letter_quantity
                    # trzeba przemnożyć przez ilość wystąpień litery odgadniętej

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
