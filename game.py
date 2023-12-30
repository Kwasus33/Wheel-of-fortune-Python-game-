from player import Player
from Words import Words, Word
from Wheel_of_fortune import Wheel_of_fortune
from Utilities import clear_char, clear_word
from database import Database
from Words import CONSONANTS, VOCALS
import random
import inputimeout


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

    def insert_Vocal_or_Consonant(self, value):

        if value is None:
            letter = clear_char(input(str())).upper()
            while letter not in VOCALS:
                print('Value is invalid. Give a vocal to guess')
                letter = clear_char(input(str())).upper()

        else:
            letter = clear_char(input(str())).upper()
            while letter not in CONSONANTS:
                print('Value is invalid. Give a consonant to guess')
                letter = clear_char(input(str())).upper()

        return letter

    def guess_letter(self, player: Player, value=None):

        good_guess = False
        consonant_info = 'Guess a consonant'
        vocal_info = 'Guess a vocal'

        print(vocal_info) if value is None else print(consonant_info)

        letter = self.insert_Vocal_or_Consonant(value)

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

    def guess_word(self):
        word_guess = clear_word(input(str('Guess the word'))).upper()
        if word_guess == self.word:
            print('Your guess is correct, you win the round')
            good_guess = True
            self.letters_to_guess = {}
            self.word_repr = self.word
        else:
            print('Your guess is not correct')
            good_guess = False
        return good_guess

    def choose_vocal(self, player):
        # muszę jakoś zabezpieczyć żeby
        # litera podawana była samogłoską
        player.add_to_balance(-200)
        good_guess = self.guess_letter(player)
        return good_guess

    def buy_vocal(self, player):
        if player.balance() > 200:
            good_guess = self.choose_vocal(player)
            answer = None
            # setting answer to empty string allows player
            # to chose different option in every loop
        else:
            while answer not in ['S', 'G']:
                print("You do not have enough money to buy a vocal")
                print("Press S if u want to spin a wheel" + '\n' +
                      "Press G if u want to guess the word" + '\n')
                answer = clear_char(input(str())).upper()
        return answer, good_guess

    def choose_action(self, answer):
        while answer not in ['B', 'S', 'G']:
            print("Press B if u want to buy a vocal" + '\n' +
                  "Press S if u want to spin a wheel" + '\n' +
                  "Press G if u want to guess the word" + '\n')
            answer = clear_char(input(str())).upper()
        return answer

    def win_money(self, value, player):
        """

        """
        good_guess = self.guess_letter(player, value)
        answer = None

        while good_guess:
            # if all letters are guessed - self.letters_to_guess is empty
            # loop ends and func returns
            print(self.word_repr)

            if self.letters_to_guess:

                answer = self.choose_action(answer)

                if answer == 'B':
                    answer, good_guess = self.buy_vocal(player)
                    # jeśli tu będzie good_guess = false to zostanie zwrócone
                    # false po wyjściu z pętli while good_guess

                elif answer == 'G':
                    return self.guess_word()

                else:
                    # returns True if player wants to spin the wheel,
                    # it returns to play(), where spin is held
                    return good_guess

            else:
                return good_guess

        return good_guess
        # returns only (if) good_guess = False

    def play(self, idx):

        id = idx % len(self._players)
        self.word_repr = self._word_object.letter_repr()

        print('\n' + self._word_object.category)
        print(self.word_repr + '\n')

        while self.letters_to_guess:

            id = (id % len(self._players))
            player = self._players[id]

            print(f'Player {player.id} turn')
            print('Press any button to spin the wheel')
            input()

            wheel_item = self._wheel.spin_wheel()
            value = wheel_item.word
            # wheel_item is instance of word class
            print(value)

            if value == 'BANKRUT':
                player.set_balance(0)
                id += 1
            elif value == 'STOP':
                id += 1
                # gracz traci kolejkę
            else:
                if not self.win_money(str(value), player):
                    id += 1
                # jeśli zwróci false to znaczy że gracz traci kolejkę
                # jeśli nie to ponownie kręci kołem

            print(self.word_repr + '\n')

        print('\n' + "There's no more consonants in the word" + '\n')

        while self.word_repr != self.word:

            id = (id % len(self._players))
            player = self._players[id]

            print(f'Player {player.id} turn')

            answer = None
            while answer not in ['B', 'G']:
                print("Press B if u want to buy a vocal" + '\n' +
                      "Press G if u want to guess the word" + '\n')
                answer = clear_char(input(str())).upper()

            if answer == 'B':
                answer, good_guess = self.buy_vocal(player)
                if not good_guess:
                    id += 1

            elif answer == 'G':
                # self.guess_word() returns false if gueesed word is incorect
                if not self.guess_word(good_guess):
                    id += 1

        player.add_to_total_balance(player.balance())

        player_info = player.id

        print(f'Player {player_info} wins the round')

        for player in self._players:
            player.set_balance(0)
            print(f'Player {player.id}')
            print(player.total_balance())


class Final():
    def __init__(self, best_player: Player, final_word: Word) -> None:
        self._best_player = best_player

        drawn_letters = random.choice(CONSONANTS, k=3)
        drawn_letters = random.choice(VOCALS, k=2)
        self._word = final_word

        self.drawn_letters = drawn_letters

    def choose_letters_set(self):
        print(f'Drawn set of values is: {self.drawn_letters}')
        print('Choose first 3 consonants, then 1 vocal')

        for i in range(3):
            letter = clear_char(input(str('Choose a consonant'))).upper()
            while letter not in CONSONANTS:
                print('Given invalid value - not a consonant')
                letter = clear_char(input(str('Choose a consonant'))).upper()
            self.drawn_letters.append(letter)

        letter = clear_char(input(str('Choose a vocal'))).upper()
        while letter not in VOCALS:
            print('Given invalid value - not a vocal')
            letter = clear_char(input(str('Choose a vocal'))).upper()
        self.drawn_letters.append(letter)

    def play_final(self) -> None:

        self.choose_letters_set()
        word_repr = self._word.letter_repr()

        for letter in self.drawn_letters:
            word_repr = self._word.update_letter_repr(word_repr, letter)

        guess_word = None
        try:
            guess_word = str(clear_word(inputimeout(
                prompt='You have 20 secunds to guess the word',
                timeout=20))).upper()

            if guess_word == self._word.word:
                print(f"You guessed correctly. The word is {guess_word}")
                result = 'You won Polonez'
                return result
            else:
                print("You didn't guess correctly")

        except Exception:
            print("You've run out of time")

        result = 'You lost the final'
        return result
