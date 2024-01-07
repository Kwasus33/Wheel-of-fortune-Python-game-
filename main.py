from settings import choose_game_mode
from settings import prepare_game


def main():

    game_mode = choose_game_mode()
    prepare_game(game_mode)


if __name__ == "__main__":
    main()
