from Utilities import clear_word, cls
from game import GameConfiguration


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
        answer = clear_word(input(str()))
        if answer not in ['1', '2', '3']:
            cls()
            print("Incorrect game mode given, choose value from [1, 2, 3]\n")
    return answer


def give_file_path(number_of_rounds: int) -> str:
    """
    Players give a path to a file with words
    """
    print("Give a path to file with words to draw during game (.txt or .json)")
    print(f"Number of words in file must be minimum {number_of_rounds + 1}")
    answer = clear_word(input(str()))
    return answer


def config_game(players_number: int,
                rounds_number: int = 3) -> "GameConfiguration":
    """
    Manages whole gameplay,
    Creates instances of GameConfiguration, GameRound and Final
    """
    words_path = give_file_path(rounds_number)

    if players_number == 1:
        game_config = GameConfiguration(words_path)
    else:
        game_config = GameConfiguration(words_path, players_number)

    if len(game_config.words()) < (rounds_number + 1):
        raise NotEnoughWordsError("You cannot play the game.\n"
                                  "Given file with words to guess during "
                                  "gameplay has too little values")
    return game_config


def prepare_game(game_mode: str) -> ("GameConfiguration", int):
    """
    Depending on chosen game mode, calls prepare_game() function
    Game mode 1: 1 player, 3 rounds + final
    Game mode 2: 3 players, 3 rounds + final
    Game mode 3: given number of players (2-6),
                 number rounds same as number of players + final
    """
    if game_mode == '1':
        config = config_game(1)
        rounds_number = 3
    elif game_mode == '2':
        config = config_game(3)
        rounds_number = 3
    elif game_mode == '3':
        players_number = 0
        while players_number <= 1 or players_number > 6:
            print('Give a valid number of players [2-6 players]')
            try:
                players_number = int(clear_word(input()))
            except ValueError:
                print('Value have to be a number')
        config = config_game(players_number, players_number)
        rounds_number = players_number
    else:
        raise Exception("Given wrong 'game mode' option")
    return config, rounds_number
