from game import Player, GameRound, Final
from Wheel_of_fortune import Wheel_of_fortune
# from Words import Words
from Utilities import clear_word, read_from_csv


def main():

    n = 0
    players = []

    while n <= 0:
        try:
            n = int(clear_word(input(int('Podaj liczbę graczy [2-6 graczy]'))))
        except TypeError:
            print('Value have to be a number between 2 - 6')

    for idx in range(n):
        players.append(Player(idx+1))

    value_list = read_from_csv('values.txt')
    wheel = Wheel_of_fortune(value_list)

    round1 = GameRound()
    round2 = GameRound()
    round3 = GameRound()

    final = Final()


if __name__ == "__main__":
    main()
