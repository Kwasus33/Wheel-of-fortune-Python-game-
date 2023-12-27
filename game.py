from player import Player
from Words import Words, Word
from Wheel_of_fortune import Wheel_of_fortune
from Utilities import clear_char
from database import Database


class GameMenu():
    def __init__(self, path: str, num_of_players: int = 1) -> None:
        self._players_num = num_of_players
        self._path = path
        self._words = Words(Database().load_from_file(self._path))

    @property
    def get_players(self) -> list:
        players = []
        for idx in range(self._players_num):
            players.append(Player(idx+1))
        return players

    def words(self) -> Words:
        return self._words

    def get_wheel_of_forune(self) -> Wheel_of_fortune:
        return Wheel_of_fortune(Database().load_from_file('values.txt'))

    def get_word(self):
        word = self._words.draw_word()
        self._words.words.remove(word)
        return word


class GameRound():
    def __init__(self, players: list["Player"],
                 word: Word,
                 wheel: Wheel_of_fortune) -> None:
        self._players = players
        self._word_object = word
        self.category = word.category
        self.word = word.word
        self.word_repr = word.letter_repr()
        self._wheel = wheel
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
        print(int(value))
        if player.balance() > 200:
            print("Press T if u want to buy a vocal, else any other button")
            answer = clear_char(input(str())).upper()
        else:
            print("You cannot buy a vocal")
            answer = None

        if answer == 'T':
            letter = self.buy_vocal(player)
            if letter in letters_in_word:
                self.word_repr = self._word_object.update_letter_repr(
                    self.word_repr, letter)
                letters_in_word.pop(letter)
        else:
            letter = clear_char(input(str())).upper()
            if letter in letters_in_word:
                self.word_repr = self._word_object.update_letter_repr(
                    self.word_repr, letter)
                amount = letters_in_word[letter] * value
                player.add_to_balance(amount)
                letters_in_word.pop(letter)
                # player to ma być obiekt klasy Player,
                # zawodnik który aktualnie zgaduje
        return letters_in_word

    def play(self):

        letters_in_word = self._word_object.letters_dict
        self.word_repr = self._word_object.letter_repr()
        id = 0
        print(self.word_repr)

        # while '_' in word_repr
        while letters_in_word:

            id = (id % self._numb_of_players)
            player = self._players[id]

            print(f'Player {player.id} turn')
            print('Press anhy button to spin the wheel')
            input()
            wheel_item = self._wheel.spin_wheel()
            value = wheel_item.word
            # wheel_item is instance of word class

            if value == 'BANKRUT':
                print(value)
                player.set_balance(0)
                id += 1
            elif value == 'NAGRODA':
                print(value)
                # losowanie nazwy nagrody z pliku i
                # dodawanie do listy nagród gracza
            elif value == 'STOP':
                print(value)
                id += 1
                # gracz traci kolejkę
            else:
                letters_in_word = self.GET_MONEY(int(value),
                                                 letters_in_word,
                                                 player)

            print(self.word_repr)

        for player in self._players:
            print(player.balance())


class Final():
    pass
