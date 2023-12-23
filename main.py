from Wheel_of_fortune import Wheel_of_fortune
from Words import Words
from Utilities import read_from_file, clear_letter_repr, read_from_csv


if __name__ == "__main__":

    value_list = read_from_csv('values.txt')
    wheel = Wheel_of_fortune(value_list)

    round1 = game_round()
    round2 = game_round()
    round3 = game_round()

    final = final()