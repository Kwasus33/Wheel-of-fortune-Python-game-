from game import GameMenu, GameRound, Final
from Utilities import clear_word


def main():

    players_number = 0

    while players_number <= 1 or players_number > 6:
        print('Give a valid number of players [2-6 players]')
        try:
            players_number = int(clear_word(input()))
        except TypeError:
            print('Value have to be a number between 2 - 6')

    menu = GameMenu('words.txt', players_number)
    players = menu.get_players
    wheel = menu.get_wheel_of_forune()

    for idx in range(3):
        word = menu.get_word()
        GameRound(players, word, wheel).play(idx)

    Final()

    # for round in range(3):
    #     for word_og in menu.check_words().words:
    #         print(word_og.word)
    #     word = menu.get_word()
    #     print('\n' + word.word + '\n')

    # for word_og in menu.check_words().words:
    #     print(word_og.word)


if __name__ == "__main__":
    main()
