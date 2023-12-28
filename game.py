from player import Player
from Words import Words, Word
from Wheel_of_fortune import Wheel_of_fortune
from Utilities import clear_char, clear_word
from database import Database
from Words import CONSONANTS, VOCALS


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

    def get_wheel_of_forune(self,
                            path: str = 'values.txt') -> Wheel_of_fortune:
        return Wheel_of_fortune(Database().load_from_file(str(path)))

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
        self._wheel = wheel
        self.word = word.word

        self.letters_to_guess = {}

        for letter in self.word:
            if letter != ' ' and letter in CONSONANTS:
                if letter not in self.letters_to_guess:
                    self.letters_to_guess[str(letter)] = 1
                else:
                    self.letters_to_guess[str(letter)] += 1

    @property
    def players(self):
        return self._players

    def guess_letter(self, player: Player, value=None):

        good_guess = False
        consonant_info = f'{value}\nGuess a consonant'
        vocal_info = 'Guess a vocal'

        print(consonant_info) if value is not None else print(vocal_info)
        letter = clear_char(input(str())).upper()

        if letter in self.word:
            good_guess = True
            self.word_repr = self._word_object.update_letter_repr(
                self.word_repr, letter)
            if letter in CONSONANTS:
                if value.isnumeric():
                    amount = self.letters_to_guess[letter] * int(value)
                    player.add_to_balance(amount)
                else:
                    player.add_reward(value)
                    # tu dodaje nagrodę do ekwipunku gracza
                self.letters_to_guess.pop(letter)

        return good_guess

    def guess_word(self, good_guess):
        word_guess = clear_word(input(str('Guess the word'))).upper()
        if word_guess == self.word:
            print('Your guess is correct, you win the round')
            self.letters_to_guess = {}
            self.word_repr = self.word
        else:
            print('Your guess is not correct')
            good_guess = False
        return good_guess

    def buy_vocal(self, player):
        # muszę jakoś zabezpieczyć żeby
        # litera podawana była samogłoską
        player.add_to_balance(-200)
        good_guess = self.guess_letter(player)
        return good_guess

    def win_money(self, value, player):
        """

        """
        print(self.word_repr)
        good_guess = self.guess_letter(player, value)
        answer = ''

        while good_guess:
            # if all letters are guessed - self.letters_to_guess is empty
            # loop ends and func returns

            print(self.word_repr)
            if self.letters_to_guess:

                while answer not in ['B', 'S', 'G']:
                    print("Press B if u want to buy a vocal" + '\n' +
                          "Press S if u want to spin a wheel" + '\n' +
                          "Press G if u want to guess the word" + '\n')
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
                    return self.guess_word(good_guess)
                    # word_guess = clear_word(input(str('Guess the word'))).upper()
                    # if word_guess == self.word:
                    #     print('Your guess is correct, you win the round')
                    #     self.letters_to_guess = {}
                    #     self.word_repr = self.word
                    # else:
                    #     print('Your guess is not correct')
                    #     good_guess = False
                    # return good_guess

                else:
                    # returns True if player wants to spin the wheel,
                    # it returns to play(), where spin is held
                    return good_guess

            return good_guess

        return good_guess
        # returns only (if) good_guess = False

    def play(self, idx):

        id = idx % len(self._players)
        self.word_repr = self._word_object.letter_repr()
        print(self._word_object.category)
        print(self.word_repr)

        while self.letters_to_guess:

            id = (id % len(self._players))
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
                if not self.win_money(str(value), player):
                    id += 1
                # jeśli zwróci false to znaczy że gracz traci kolejkę
                # jeśli nie to ponownie kręci kołem

            print(self.word_repr)

        player.add_to_total_balance(player.balance())

        for player in self._players:
            player.set_balance(0)
            print(player.total_balance())


class Final():
    pass
