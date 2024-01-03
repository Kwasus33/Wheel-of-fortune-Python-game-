from Utilities import clear_char, clear_word
from game import GameMenu, GameRound, Final
from Wheel_of_fortune import Wheel_of_fortune


class NotEnoughWordsError(Exception):
    pass


def choose_game_mode() -> str:
    """
    Players choose game mode
    """
    answer = None
    mode3_info = "(2-6 players, number of players is number of rounds + final"
    while answer not in ['1', '2', '3']:
        print("Press 1 to choose Training mode (1 player, 3 rounds + final)\n"
              "Press 2 to choose Standard mode (3 players, 3 rounds + final)\n"
              f"Press 3 to choose Custome mode\n{mode3_info}\n")
        answer = clear_char(input(str()))
    return answer


def give_file_path(number_of_rounds: int) -> str:
    """
    Players give a path to a file with words
    """
    print("Give a path to file with words to draw during game (.txt or .json)")
    print(f"Number of words in file must be minimum {number_of_rounds + 1}")
    answer = clear_word(input(str()))
    return answer


def choose_wheel_path(menu: GameMenu) -> Wheel_of_fortune:
    """
    Choose if wheel of fortune have default or own values, read from file
    """
    print("Press T to give a path to a file with own wheel of fortune values")
    print("Else press any other value")
    answer = clear_char(input(str())).upper()
    if answer == 'T':
        print("Give path to that file")
        path = clear_word(input(str()))
        return menu.get_wheel_of_forune(path)
    else:
        return menu.get_wheel_of_forune()


def set_game_mode(players_number: int, rounds_number: int = 3) -> None:
    """
    Manages whole gameplay, creates instances of GameMenu, GameRound and Final
    """
    words_path = give_file_path(rounds_number)
    training_menu = GameMenu(words_path)
    standard_menu = GameMenu(words_path, players_number)
    menu = training_menu if players_number == 1 else standard_menu
    if len(menu.check_words().words) < (rounds_number + 1):
        raise NotEnoughWordsError("You cannot play the game.\n"
                                  "Given file with words to guess during "
                                  "gameplay has too little values")
    players = menu.get_players
    wheel = choose_wheel_path(menu)

    for idx in range(rounds_number):
        word = menu.get_word()
        GameRound(players, word, wheel).play(idx)

    word = menu.get_word()
    final = Final(players, word)
    print(final.play_final())


def training_game_mode() -> None:
    """
    Game Mode to train skills, gameplay of 3 rounds + final for 1 player
    """
    set_game_mode(1)


def standard_game_mode() -> None:
    """
    Standard gameplay - 3 players, 3 rounds + final
    """
    set_game_mode(3)


def custom_game_mode() -> None:
    """
    Game can be played by 2 to 6 players
    There is as many rounds as players + final
    """
    players_number = 0
    while players_number <= 1 or players_number > 6:
        print('Give a valid number of players [2-6 players]')
        try:
            players_number = int(clear_word(input()))
        except ValueError:
            print('Value have to be a number between 2 - 6')

    set_game_mode(players_number, players_number)
