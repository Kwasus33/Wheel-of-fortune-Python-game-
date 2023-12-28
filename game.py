from player import Player
from Words import Words, Word
from Wheel_of_fortune import Wheel_of_fortune
from Utilities import clear_char, clear_word
from database import Database


class GameMenu():
    def __init__(self, path: str, num_of_players: int = 1) -> None:
        self._players_num = num_of_players
        self._path = path
        self.words = Words(Database().load_from_file(self._path))

    @property
    def get_players(self) -> list:
        players = []
        for idx in range(self._players_num):
            players.append(Player(idx+1))
        return players

    def check_words(self) -> Words:
        return self.words

    def get_wheel_of_forune(self) -> Wheel_of_fortune:
        return Wheel_of_fortune(Database().load_from_file('values.txt'))

    def get_word(self) -> Word:
        word = self.words.draw_word()
        self.words.words.remove(word)
        return word


class GameRound():
    def __init__(self, players: list["Player"],
                 word: Word,
                 wheel: Wheel_of_fortune) -> None:
        self._players = players
        self._word_object = word
        self.letters_in_word = self._word_object.letters_dict
        self.category = word.category
        self.word = word.word
        self.word_repr = word.letter_repr()
        self._wheel = wheel
        self._numb_of_players = len(self._players)

    @property
    def players(self):
        return self._players

    def buy_vocal(self, player):
        player.add_to_balance(-200)
        good_guess = self.guess_letter(player)
        return good_guess

    def guess_letter(self, player: Player, value=0):

        good_guess = False
        consonant_info = f'{value}\nGuess a consonant'
        vocal_info = 'Guess a vocal'

        print(consonant_info) if value != 0 else print(vocal_info)
        letter = clear_char(input(str())).upper()

        if letter in self.letters_in_word:
            good_guess = True
            self.word_repr = self._word_object.update_letter_repr(
                self.word_repr, letter)
            if value != 0:
                if value.isnumeric():
                    amount = self.letters_in_word[letter] * int(value)
                    player.add_to_balance(amount)
            else:
                player.add_reward(value)
                # tu dodaje nagrodę do ekwipunku gracza
            self.letters_in_word.pop(letter)

        return good_guess

    def GET_MONEY(self, value, player):
        """

        """
        good_guess = self.guess_letter(player, value)
        answer = ''

        # have to add condition ending the func if all letters are guseed

        while good_guess:

            while answer not in ['B', 'S', 'G']:
                print("Press B if u want to buy a vocal" + '\n' +
                      "Press S if u want to spin a wheel" + '\n' +
                      "Press G if u want to guess the word")
                answer = clear_char(input(str())).upper()

            if answer == 'B':
                if player.balance() > 200:
                    good_guess = self.buy_vocal(player)
                    answer = ''
                    # setting answer to empty string allows player
                    # to chose different option in every loop
                else:
                    while answer not in ['S', 'G']:
                        print("You do not have enough money to buy a vocal")
                        print("Press S if u want to spin a wheel" + '\n' +
                              "Press G if u want to guess the word")
                        answer = clear_char(input(str())).upper()

            elif answer == 'G':
                word_guess = clear_word(input(str('Guess the word'))).upper()
                if word_guess == self.word:
                    print('Your guess is correct, you win the round')
                    self.letters_in_word = {}
                    self.word_repr = self.word
                else:
                    print('Your guess is not correct')
                    good_guess = False
                return good_guess

            else:
                # returns True if player wants to spin the wheel,
                # it returns to play(), where spin is held
                return True

        return good_guess
        # returns only (if) good_guess = False

    def play(self):

        self.word_repr = self._word_object.letter_repr()
        id = 0
        print(self.word_repr)

        # while '_' in word_repr
        while self.letters_in_word:

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
            elif value == 'STOP':
                print(value)
                id += 1
                # gracz traci kolejkę
            else:
                if not self.GET_MONEY(str(value), player):
                    id += 1
                # jeśli zwróci false to znaczy że gracz traci kolejkę
                # jeśli nie to ponownie kręci kołem

            print(self.word_repr)

        for player in self._players:
            print(player.balance())


class Final():
    pass
