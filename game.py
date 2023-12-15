# from Wheel_of_fortune import Wheel_of_fortune
# from Words import Words
# from Utilities import read_from_file, clear_letter_repr


if __name__ == "__main__":

    pass

    # list_of_all_letter_objects = read_from_file('values.txt')
    # wheel = Wheel_of_fortune(list_of_all_letter_objects)
    # drawn_word = Words(read_from_file('words.txt')).random_choice()
    # current_letter_repr = str(drawn_word.letter_representation())
    # print(drawn_word.word)
    # letters_in_word = drawn_word._letters_list

    # while letters_in_word != []:
    #     print(current_letter_repr)
    #     letter = wheel.random_choice()
    #     print(letter)
    #     current_letter_repr = clear_letter_repr(current_letter_repr)
    #     info = drawn_word.update_letter_representation(current_letter_repr,
    #                                                    letter)
    #     current_letter_repr = str(info)
    #     if letter in letters_in_word:
    #         letters_in_word.remove(str(letter))
    #     for letter_obj in list_of_all_letter_objects:
    #         if letter_obj.word == letter:
    #             list_of_all_letter_objects.remove(letter_obj)

    # print(current_letter_repr)
