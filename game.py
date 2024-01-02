from player import Player
from Words import Words, Word
from Wheel_of_fortune import Wheel_of_fortune
from Utilities import clear_char, clear_word
from database import Database
from Words import CONSONANTS, VOCALS
import random
import pytimedinput
# import threading


class GameMenu():
    """
    Class GameMenu contains atributes:

    param players_num: number of players in game, defaults to 1
    type players_num: int

    param path: path to file with words to draw from during game
    type path: str

    param words: object of class Words,
    which atribute is list of objects of Word class
    type words: class Words
    """
    def __init__(self, path: str, num_of_players: int = 1) -> None:
        """
        Creates instance of GameMenu
        """
        self._players_num = num_of_players
        self._path = path
        self.words = Words(Database().load_from_file(self._path))

    @property
    def get_players(self) -> list:
        """
        Creates players as Player class objects
        and returns a list of them
        """
        players = []
        for idx in range(self._players_num):
            players.append(Player(idx+1))
        return players

    def check_words(self) -> Words:
        """
        Returns object of class Words,
        containing all words that can be drawn
        """
        return self.words

    def get_wheel_of_forune(self,
                            path: str = 'values.txt') -> Wheel_of_fortune:
        """
        Creates and returns an object of class Wheel_of_fortune with
        values from given path, defaults to values.txt (standard values)
        """
        return Wheel_of_fortune(Database().load_from_file(str(path)))

    def get_word(self) -> Word:
        """
        Draws and returns a Word object from Words object
        Removes drawn Word from Words, so it cannot be drawn more than once
        """
        word = self.words.draw_word()
        self.words.words.remove(word)
        return word


class GameRound():
    """
    Class GameRound contains atributes:

    param players: list of players
    type players: list of class Player objects

    param word_object: contains word to guess and it's category
    type word_object: class Word object

    param word: word to guess, word_object instance atribute
    type word_object: str

    param wheel: have methode to spin and return drawn value
    type wheel: class Wheel_of_fortune object

    param word_repr: current representation of a drawn word to guess
    type word_repr: str

    param id: id/position on a list of a player whose turn is at that moment
    type id: int

    param letter_guesses: contains all already tried letters, to not repeat any
    type letter_guesses: list

    param word_consonants: contains quantity of all consonants in drawn word
    type word_consonants: dict{consonant: quantity}
    """
    def __init__(self, players: list["Player"],
                 word: Word,
                 wheel: Wheel_of_fortune) -> None:
        """
        Creates instance of GameRound
        """
        self._players = players
        self._word_object = word
        self._wheel = wheel
        self.word = word.word
        self.word_repr = self._word_object.word_repr()
        self.id = None

        self.letter_guesses = []

        self.word_consonants = {}

        for letter in self.word:
            if letter in CONSONANTS:
                if letter in self.word_consonants:
                    self.word_consonants[letter] += 1
                else:
                    self.word_consonants[letter] = 1

    @property
    def players(self):
        "Returns list of players"
        return self._players

    def insert_Vocal_or_Consonant(self, value):
        """
        Player inserts letter, func checks if given letter is correct
        """
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

    def guess_letter(self, player: Player, value: str = None):
        """
        Player chooses a letter, if letter is in word,
        word underscape representation is updated
        if letter is consonant and in word, player earns drawn money
        """
        good_guess = False
        consonant_info = 'Guess a consonant'
        vocal_info = 'Guess a vocal'

        print(vocal_info) if value is None else print(consonant_info)

        letter = self.insert_Vocal_or_Consonant(value)

        while letter in self.letter_guesses:
            print('Letter has been already given. Choose different one')
            letter = self.insert_Vocal_or_Consonant(value)

        self.letter_guesses.append(letter)

        if letter in self.word:
            good_guess = True
            self.word_repr = self._word_object.word_repr(self.letter_guesses)
            if letter in CONSONANTS:
                if value.isnumeric():
                    amount = self.word_consonants[letter] * int(value)
                    player.add_to_balance(amount)
                else:
                    player.add_reward(value)
                    # tu dodaje nagrodę do ekwipunku gracza
                self.word_consonants.pop(letter)

        return good_guess

    def guess_word(self):
        """
        Returns True if player correctly guesses the word, else False
        """
        word_guess = clear_word(input(str('Guess the word'))).upper()
        if word_guess == self.word:
            print('Your guess is correct, you win the round')
            good_guess = True
            self.word_consonants = {}
            self.word_repr = self.word
        else:
            print('Your guess is not correct')
            good_guess = False
        return good_guess

    def choose_vocal(self, player: Player):
        """
        Decreases players balance by 200, after buying a vocal
        returns True if bought vocal is in the word, else False
        """
        player.add_to_balance(-200)
        good_guess = self.guess_letter(player)
        return good_guess

    def buy_vocal(self, player: Player, can_spin_wheel: bool = True):
        """
        Allows player to buy vocal if have enought money,
        else force player to choose to spin the wheel or guess the word
        """
        answer = None
        good_guess = True
        # good_guess = True returns if bought vocal is correct
        # or when player has not enough money to buy a vocal,
        # in second situation player doesn't lose a turn
        if player.balance() > 200:
            good_guess = self.choose_vocal(player)
            # setting answer to empty string allows player
            # to chose different option in every loop
        else:
            range = ['S', 'G'] if can_spin_wheel else ['G']
            while answer not in range:
                print("You do not have enough money to buy a vocal\n")
                if can_spin_wheel:
                    print("Press S if u want to spin a wheel")
                print("Press G if u want to guess the word\n")
                answer = clear_char(input(str())).upper()
        return answer, good_guess

    def choose_action(self, answer):
        """
        Returns player's choice - buy a vocal, spin the wheel or guess the word
        """
        while answer not in ['B', 'S', 'G']:
            print("Press B if u want to buy a vocal" + '\n' +
                  "Press S if u want to spin the wheel" + '\n' +
                  "Press G if u want to guess the word" + '\n')
            answer = clear_char(input(str())).upper()
        return answer

    def win_money(self, value, player):
        """
        First player guesses a consonant
        If guess is in word_consonants player can buy a vocal,
        guess the word, or spin the wheel
        """
        # CZY DODAWAĆ TO DO DOKUMENTACJI
        # Player plays while guesses are correct - good_guess = True
        # Returns False, when guessed consonant or bought vocal is incorect
        # Returns True, when guessed word is correct
        # Returns True when player chooses to spin the wheel

        good_guess = self.guess_letter(player, value)
        answer = None

        while good_guess:
            # if all letters are guessed - self.word_consonants is empty
            # loop ends and func returns
            print(self.word_repr)

            if self.word_consonants:

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

    def wheel_spin(self):
        """
        Allows player to spin the wheel
        Maintains forward actions dependent on drawn value
        Returns currently playing player instance
        """
        self.id = (self.id % len(self._players))
        player = self._players[self.id]

        print(f'Player {player.id} turn')

        print('Press any button to spin the wheel')
        input()

        wheel_item = self._wheel.spin_wheel()
        value = wheel_item.word
        # wheel_item is instance of word class
        print(value)

        if value == 'BANKRUT':
            player.set_balance(0)
            self.id += 1
        elif value == 'STOP':
            self.id += 1
            # gracz traci kolejkę
        else:
            if not self.win_money(value, player):
                self.id += 1
            # jeśli zwróci false to znaczy że gracz traci kolejkę
            # jeśli nie to ponownie kręci kołem
        print(self.word_repr + '\n')

        return player

    def play(self, idx):
        """
        Players spin the wheel till all consonants are guessed
        Returns if the word is guessed - one of the players wins the round
        """
        self.id = idx
        # self.word_repr = self._word_object.word_repr()
        # pierwsza repr zadeklarowana w konstruktorze

        print('\n' + self._word_object.category)
        print(self.word_repr + '\n')

        while self.word_consonants:
            player = self.wheel_spin()

        if self.word_repr != self.word:
            print('\n' + "There's no more consonants in the word" + '\n')
            print(self.word_repr)

        # muszę to jakoś poprawić

        while self.word_repr != self.word:

            self.id = (self.id % len(self._players))
            player = self._players[self.id]

            print(f'Player {player.id} turn')

            answer = None
            while answer not in ['B', 'G']:
                print("Press B if u want to buy a vocal" + '\n' +
                      "Press G if u want to guess the word" + '\n')
                answer = clear_char(input(str())).upper()

            if answer == 'B':
                answer, good_guess = self.buy_vocal(player, False)
                if not good_guess:
                    self.id += 1

            elif answer == 'G':
                # self.guess_word() returns false if gueesed word is incorect
                if not self.guess_word():
                    self.id += 1

            print(self.word_repr)

        print(f"\nThe answer is '{self.word_repr}'\n")

        player_info = player.id

        print(f'\nPlayer {player_info} wins the round\n')

        player.add_to_total_balance(player.balance())

        for player in self._players:
            player.set_balance(0)
            print(f'Player {player.id}')
            print(f'{player.total_balance()}\n')


# class Final(GameRound):
class Final():
    """
    Class Final contains atributes:

    param players: list of players
    type players: list of class Player objects

    param word: contains word to guess and it's category
    type word: class Word object

    param drawn_letters: letters drawn and chosen by player that will be
                         displayed in undersacpe representation of a drawn word
    type drawn_letters: list
    """
    def __init__(self, players: list[Player], final_word: Word) -> None:
        """
        Creates instance of Final
        """
        # super.__init__(players, final_word)
        self._players = players
        self._word = final_word

        drawn_letters = random.sample(CONSONANTS, 3) + random.sample(VOCALS, 2)

        self.drawn_letters = drawn_letters

    def best_player(self):
        """
        Returns a list of best players
        One who have the highest balance
        if several have same balance, one who have the most rewards
        if several have same balance and same number of rewards, returns each
        """
        best_players = []
        players = sorted(self._players,
                         key=lambda player: player.total_balance())
        best_player = players.pop()
        # bierze ostatni element z listy posortowanej rosnąco, czyli maksymalny
        best_players.append(best_player)

        for player in players:
            if player.total_balance() == best_player.total_balance():
                best_players.append(player)

        if len(best_players) > 1:

            best_players_with_most_gifts = []
            most_gifts_list = sorted(best_players,
                                     key=lambda player: len(player.reward()))
            most_gifts_player = most_gifts_list.pop()
            best_players_with_most_gifts.append(most_gifts_player)

            for player in most_gifts_list:
                if len(player.reward()) == len(most_gifts_player.reward()):
                    best_players_with_most_gifts.append(player)

            return best_players_with_most_gifts

        return best_players

    def choose_letters_set(self):
        """
        Updates set of letters to expose if in word
        by 3 consonants and 1 vocal chosen by player
        """
        print(f'Drawn set of values is: {self.drawn_letters}')
        print('Choose first 3 consonants, then 1 vocal')

        for i in range(3):
            info = 'first' if i == 0 else 'second' if i == 1 else 'third'
            letter = clear_char(input(str(f'Choose {info} consonant'))).upper()
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
        """
        Informs which Player plays final round
        Player gives set of own letters, letters in word are exposed
        Player has 20 seconds to give the answer
        Returns information about the final result
        """
        best_players = self.best_player()
        if len(best_players) != 1:
            return "There is none best player. Final round can't be played"
        best_player = best_players.pop()
        print(f"Player {best_player.id} plays the Final Round")

        self.choose_letters_set()
        word_repr = self._word.word_repr(self.drawn_letters)

        print(self._word.category + '\n' + word_repr)

        answer, timedOut = pytimedinput.timedInput(
            prompt="You have 20 seconds to guess the word\n",
            timeout=10)

        answer = clear_word(str(answer)).upper()

        if timedOut:
            print("Time's up.")
        print(f"Player's answer is: '{answer}'")

        if answer == self._word.word:
            print(f"You guessed correctly. The word is {self._word.word}")
            result = 'You won Polonez'

        else:
            print(f"You didn't guess the word. It is {self._word.word}")
            result = 'You lost the final'

        return result
