from player import Player
from Words import Word
from Wheel_of_fortune import Wheel_of_fortune
from Utilities import clear_word, cls
from database import Database
from Words import CONSONANTS, VOCALS
import random
import pytimedinput


class GameConfiguration():
    """
    Class GameConfiguration contains atributes:

    param players_num: number of players in game, defaults to 1
    type players_num: int

    param path: path to file with words to draw from during game
    type path: str

    param words: list of words read from given path to file
    type words: list of class Word objects
    """
    def __init__(self, path: str, num_of_players: int = 1) -> None:
        """
        Creates instance of GameConfiguration
        """
        self._players_num = num_of_players
        self._words = Database().load_from_file(path)

    def words(self) -> list["Word"]:
        """
        Returns list of class Word objects,
        contains all words that can be drawn
        """
        return self._words

    def create_players(self) -> list:
        """
        Creates players as Player class objects
        and returns a list of them
        """
        players = []
        for idx in range(self._players_num):
            players.append(Player(idx+1))
        return players

    def choose_wheel_of_fortune(self) -> "Wheel_of_fortune":
        """
        Creates and returns an object of class Wheel_of_fortune with
        values from chosen path, player can give path to own file with values,
        default path is values.txt (standard values)
        """
        print("Press T to give a path to a file with wheel of fortune values")
        print("Press any other key to choose default set of values")
        answer = clear_word(input(str())).upper()
        if answer == 'T':
            print("Give path to file with 'wheel of fortune' values")
            path = clear_word(input(str()))
        else:
            path = 'values.txt'
        return Wheel_of_fortune(Database().load_from_file(str(path)))

    def get_word(self) -> "Word":
        """
        Draws and returns a Word object from list
        Removes drawn Word from list, so it cannot be drawn more than once
        """
        word = random.choice(self._words)
        self._words.remove(word)
        return word


class GameRound():
    """
    Class GameRound contains atributes:

    param players: list of players
    type players: list of class Player objects

    param word_object: contains word to guess and it's category
    type word_object: class Word object

    param wheel: have methode to spin and return drawn value
    type wheel: class Wheel_of_fortune object

    param word_repr: current representation of a drawn word to guess
    type word_repr: str

    param player_pointer: position on a list of a player whose turn is
    type player_pointer: int

    param letter_guesses: contains all already tried letters, to not repeat any
    type letter_guesses: list

    param word_consonants: contains quantity of all consonants in drawn word
    type word_consonants: dict{consonant: quantity}
    """
    def __init__(self, players: list["Player"],
                 word: Word,
                 wheel: Wheel_of_fortune,
                 player_pointer: int) -> None:
        """
        Creates instance of GameRound
        """
        self._players = players
        self._word_object = word
        self._wheel = wheel
        self._word_repr = self._word_object.word_repr()
        self._player_pointer = player_pointer

        self._letter_guesses = []

        self._word_consonants = {}

        for letter in self._word_object.word:
            if letter in CONSONANTS:
                if letter in self._word_consonants:
                    self._word_consonants[letter] += 1
                else:
                    self._word_consonants[letter] = 1

    @property
    def players(self) -> list:
        """Returns list of players"""
        return self._players

    @property
    def wheel(self) -> "Wheel_of_fortune":
        """Returns wheel of fortune"""
        return self._wheel

    @property
    def word_object(self) -> "Word":
        """Returns word_object"""
        return self._word_object

    def word_repr(self) -> str:
        """
        Returns word_repr - word representation
        with hidden not guessed letters
        """
        return self._word_repr

    def set_word_repr(self, value: str) -> None:
        """Sets word_repr as a given value"""
        self._word_repr = value

    def word_consonants(self) -> dict:
        """Returns word_consonants"""
        return self._word_consonants

    def set_word_consonants_empty(self) -> None:
        """Sets word_consonants as empty dict"""
        self._word_consonants = {}

    def player_pointer(self) -> int:
        """Returns player pointer"""
        return self._player_pointer

    def move_player_pointer(self, shift: int):
        """Moves player pointer to point another player"""
        self._player_pointer += shift

    def set_player_pointer(self, value: int):
        self._player_pointer = value

    def letter_guesses(self) -> list:
        """Returns list of already used letters while guessing"""
        return self._letter_guesses

    def read_letter(self, value) -> str:
        """
        Player inserts letter, func checks if given letter is correct
        """
        if value is None:
            letter = clear_word(input(str())).upper()
            while letter not in VOCALS:
                print('Value is invalid. Give a vocal to guess')
                letter = clear_word(input(str())).upper()

        else:
            letter = clear_word(input(str())).upper()
            while letter not in CONSONANTS:
                print('Value is invalid. Give a consonant to guess')
                letter = clear_word(input(str())).upper()

        return letter

    def guess_letter(self, player: Player, value: str = None) -> bool:
        """
        Player chooses a letter, if letter is in word,
        word underscape representation is updated
        if letter is consonant and in word, player earns drawn money
        """
        is_good_guess = False
        consonant_info = 'Guess a consonant'
        vocal_info = 'Guess a vocal'

        print(vocal_info) if value is None else print(consonant_info)

        letter = self.read_letter(value)

        if letter in self.letter_guesses():
            print("Letter was already given. You lose a turn")
            return is_good_guess

        self.letter_guesses().append(letter)

        if letter in self.word_object.word:
            is_good_guess = True
            self.set_word_repr(
                self.word_object.word_repr(self.letter_guesses())
                )
            if letter in CONSONANTS:
                if value.isnumeric():
                    amount = self.word_consonants()[letter] * int(value)
                    player.add_to_balance(amount)
                else:
                    player.add_reward(value)
                self.word_consonants().pop(letter)
        else:
            print("Your guess is incorrect")

        return is_good_guess

    def guess_word(self) -> bool:
        """
        Returns True if player correctly guesses the word, else False
        """
        word_guess = clear_word(input(str('Guess the word\n'))).upper()
        if word_guess == self.word_object.word:
            print('\nYour guess is correct, you win the round\n')
            is_good_guess = True
            self.set_word_consonants_empty()
            self.set_word_repr(self.word_object.word)
        else:
            print('\nYour guess is not correct\n')
            is_good_guess = False
        return is_good_guess

    def buy_vocal(self, player: Player) -> bool:
        """
        Decreases players balance by 200, after buying a vocal
        returns True if bought vocal is in the word, else False
        """
        player.add_to_balance(-200)
        is_good_guess = self.guess_letter(player)
        return is_good_guess

    def give_answer(self, range: list[str]) -> str:
        """
        Returns answer chosen by a player from a given answer-range
        """
        answer = None
        while answer not in range:
            if 'B' in range:
                print("Press B if u want to buy a vocal" + '\n')
            else:
                print("You do not have enough money to buy a vocal" + '\n')
            if 'S' in range:
                print("Press S if u want to spin the wheel" + '\n')
            print("Press G if u want to guess the word" + '\n')
            answer = clear_word(input(str())).upper()
        return answer

    def choose_action(self, player: Player) -> str:
        """
        Returns player's choice from values in range -
         - buy a vocal (B), spin the wheel (S) or guess the word (G)
        """
        if player.balance() >= 200:
            if self.word_consonants():
                range = ['B', 'S', 'G']
            else:
                range = ['B', 'G']
        else:
            if self.word_consonants():
                range = ['S', 'G']
            else:
                range = ['G']
        return self.give_answer(range)

    def win_money(self, value: str, player: Player) -> bool:
        """
        First player guesses a consonant
        If guess is in word_consonants player can buy a vocal,
        guess the word, or spin the wheel
        Player plays while guesses are correct - is_good_guess = True
        Returns False, when guessed consonant or bought vocal is incorect
        Returns True, when guessed word is correct
        Returns True when player chooses to spin the wheel
        """
        is_good_guess = self.guess_letter(player, value)

        while is_good_guess:
            print(self.word_repr())
            if self.word_consonants():
                answer = self.choose_action(player)
                if answer == 'B':
                    is_good_guess = self.buy_vocal(player)
                elif answer == 'G':
                    return self.guess_word()
                elif answer == 'S':
                    return is_good_guess
                else:
                    raise Exception('Answer is out of range')
            else:
                return is_good_guess

        return is_good_guess

    def wheel_spin(self) -> Player:
        """
        Allows player to spin the wheel
        Maintains forward actions dependent on drawn value
        Returns currently playing player instance
        """
        self.set_player_pointer((self.player_pointer() % len(self.players)))
        player = self.players[self.player_pointer()]

        print('\n' + self.word_object.category)
        print(self.word_repr() + '\n')

        print(f'Player {player.id} turn')

        print('Press any button to spin the wheel')
        input()

        wheel_item = self.wheel.spin_wheel()
        value = wheel_item.word
        print(value)

        if value == 'BANKRUT':
            player.set_balance(0)
            player.remove_rewards()
            self.move_player_pointer(1)
        elif value == 'STOP':
            self.move_player_pointer(1)
        else:
            if not self.win_money(value, player):
                self.move_player_pointer(1)

        return player

    def play(self) -> None:
        """
        Players spin the wheel till all consonants are guessed
        Then can only buy a vocal or guess the word
        Returns if the word is guessed
        Player who guessed the word wins the round - keeps money and rewards
        Rest players balances are set to 0 and rewards are cleared
        """
        while self.word_consonants():
            player = self.wheel_spin()

        if self.word_repr() != self.word_object.word:
            print("\nThere's no more consonants in the word\n")
            print(f'{self.word_repr()}\n')

        while self.word_repr() != self.word_object.word:
            self.set_player_pointer(
                (self.player_pointer() % len(self.players)))
            player = self.players[self.player_pointer()]

            print(f'Player {player.id} turn\n')

            answer = self.choose_action(player)

            if answer == 'B':
                is_good_guess = self.buy_vocal(player)
                if not is_good_guess:
                    self.move_player_pointer(1)
                print(self.word_repr())
            elif answer == 'G':
                if not self.guess_word():
                    self.move_player_pointer(1)
                    print(self.word_repr())
            else:
                continue

        cls()

        print(f"\nThe answer is '{self.word_repr()}'\n")

        player_info = player.id

        print(f'\nPlayer {player_info} wins the round\n')

        player.add_to_total_balance(player.balance())
        player.set_total_rewards(player.reward())

        for player in self.players:
            player.set_balance(0)
            player.remove_rewards()
            print(f'Player {player.id}')
            print(f"Player's total balance is {player.total_balance()}")
            print(f"Player's total rewards are {player.total_rewards()}\n")


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
        self._players = players
        self._word = final_word

        self._drawn_letters = random.sample(CONSONANTS, 3)
        self._drawn_letters += random.sample(VOCALS, 2)

    @property
    def players(self):
        """Returns list of players"""
        return self._players

    @property
    def word(self):
        """Returns a word object drawn for final"""
        return self._word

    @property
    def drawn_letters(self):
        """Returns list of letters drawn for player and chosen by player"""
        return self._drawn_letters

    def find_best_player(self):
        """
        Returns a list of best players
        One who have the highest balance
        if several have same balance, one who have the most rewards
        if several have same balance and same number of rewards, returns each
        """
        best_players = []
        players = sorted(self.players,
                         key=lambda player: player.total_balance())
        best_player = players.pop()
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

            if len(best_players_with_most_gifts) != 1:
                return
            else:
                best_player = best_players_with_most_gifts.pop()

        else:
            best_player = best_players.pop()

        return best_player

    def choose_letters_set(self) -> None:
        """
        Updates set of letters to expose if in word
        by 3 consonants and 1 vocal chosen by player
        """
        print(f'Drawn set of values is: {self.drawn_letters}')
        print('Choose first 3 consonants, then 1 vocal')

        for i in range(3):
            info = 'first' if i == 0 else 'second' if i == 1 else 'third'
            letter = clear_word(
                input(str(f'Choose {info} consonant\n'))
                ).upper()
            while letter not in CONSONANTS:
                print('Given invalid value - not a consonant')
                letter = clear_word(input(str('Choose a consonant\n'))).upper()
            self.drawn_letters.append(letter)

        letter = clear_word(input(str('Choose a vocal\n'))).upper()
        while letter not in VOCALS:
            print('Given invalid value - not a vocal')
            letter = clear_word(input(str('Choose a vocal\n'))).upper()
        self.drawn_letters.append(letter)

    def play_final(self) -> str:
        """
        Player gives set of own letters, letters in word are exposed
        Player has 20 seconds to give the answer
        Returns information about the final result
        """
        best_player = self.find_best_player()

        if best_player is None:
            return "There is none best player. Final round can't be played"

        print(f"Player {best_player.id} plays the Final Round")

        self.choose_letters_set()
        word_repr = self.word.word_repr(self.drawn_letters)

        print(self.word.category + '\n' + word_repr)

        answer, timedOut = pytimedinput.timedInput(
            prompt="You have 20 seconds to guess the word\n",
            timeout=10)

        answer = clear_word(str(answer)).upper()

        if timedOut:
            print("Time's up.")
        print(f"Player's answer is: '{answer}'")

        if answer == self.word.word:
            print(f"You guessed correctly. The word is {self.word.word}")
            result = 'You won Polonez'

        else:
            print(f"You didn't guess the word. It is {self.word.word}")
            result = 'You lost the final'

        return result
