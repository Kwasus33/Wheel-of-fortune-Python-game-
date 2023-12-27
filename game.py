from Words import Words, Word
from Wheel_of_fortune import Wheel_of_fortune
from Utilities import clear_char
from database import Database


class Player():
    def __init__(self, idx: int = None) -> None:
        self._id = idx
        self._balance = 0

    @property
    def id(self):
        return self._id

    def balance(self):
        return self._balance

    def set_balance(self, amount):
        self._balance = amount

    def add_to_balance(self, amount):
        self._balance += amount


class GameMenu():
    def __init__(self, path: str, num_of_players: int = 0) -> None:
        self._players_num = num_of_players
        self._path = path

    @property
    def get_players(self) -> list:
        players = []
        for idx in range(self._players_num):
            players.append(Player(idx+1))
        return players

    def get_words(self) -> Words:
        return Words(Database().load_from_file(self._path))

    def get_wheel_of_forune(self) -> Wheel_of_fortune:
        return Wheel_of_fortune(Database().load_from_file('values.txt'))


class GameRound():
    def __init__(self, players: list["Player"], word: Word) -> None:
        self._players = players
        self._word = word
        self.word_repr = self._word.letter_repr
        self._wheel = GameMenu().get_wheel_of_forune()
        self._numb_of_players = len(self._players)

    @property
    def players(self):
        return self._players

    def buy_vocal(self, player):
        letter = clear_char(input(str())).upper()
        player.add_to_balance(-200)
        return letter

    def GET_MONEY(self, value, letters_in_word, player):
        """

        """
        print(int(value.word))
        print("Press T if u want to buy a vocal, else any other button")
        answer = clear_char(input(str())).upper()
        if answer == 'T':
            letter = self.buy_vocal(player)
            if letter in letters_in_word:
                self.word_repr = self._word.update_letter_repr(self.word_repr,
                                                               letter)
                letters_in_word.pop(letter)
        else:
            letter = clear_char(input(str())).upper()
            if letter in letters_in_word:
                self.word_repr = self._word.update_letter_repr(self.word_repr, letter)
                amount = letters_in_word[letter]*int(value.word)
                player.add_to_balance(amount)
                letters_in_word.pop(letter)
                # player to ma być obiekt klasy Player, zawodnik który aktualnie zgaduje
        return letters_in_word

    def BANKRUT(self):
        pass

    def NAGRODA(self):
        pass

    def STOP(self):
        pass

    def play(self):

        letters_in_word = self._word.letters_dict
        print(self._word.letter_repr)
        id = 0

        # while '_' in word_repr
        while letters_in_word:

            id = (id % self._numb_of_players)
            player = self._players[id]

            print(f'Player {player.id} turn')
            print('Press anhy button to spin the wheel')

            key, value = self._wheel.spin_wheel()
            # value is instance of word class

            if key == 'money':
                letters_in_word = self.GET_MONEY(value,
                                                 letters_in_word,
                                                 player)
            elif value.word == 'BANKRUT':
                print(value.word)
                player.set_balance(0)
                id += 1
            elif value.word == 'NAGRODA':
                print(value.word)
                # losowanie nazwy nagrody z pliku i dodawanie do listy nagród gracza
            elif value.word == 'STOP':
                print(value.word)
                id += 1
                # gracz traci kolejkę


class Final():
    pass
