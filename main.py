from game import GameMenu, GameRound, Final
# from Words import Words
# from Wheel_of_fortune import Wheel_of_fortune
# from Words import Words
from Utilities import clear_word


def main():

    n = 0

    while n <= 1 or n > 6:
        print('Give a valid number of players [2-6 players]')
        try:
            n = int(clear_word(input()))
        except TypeError:
            print('Value have to be a number between 2 - 6')

    menu = GameMenu(n)
    players = menu.get_players
    words, wheel = menu.game_items()
    GameRound()
    Final()


if __name__ == "__main__":
    main()
