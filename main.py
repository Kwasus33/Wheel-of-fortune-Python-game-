from settings import choose_game_mode
from settings import prepare_game
from Utilities import cls
from game import GameRound, Final


def main():

    game_mode = choose_game_mode()
    game_config, rounds_number = prepare_game(game_mode)
    players = game_config.create_players()
    wheel = game_config.choose_wheel_of_fortune()
    cls()

    for idx in range(rounds_number):
        word = game_config.get_word()
        print(f"Round {idx+1} starts")
        GameRound(players, word, wheel, idx).play()

    word = game_config.get_word()
    final = Final(players, word)
    print(final.play_final())


if __name__ == "__main__":
    main()
