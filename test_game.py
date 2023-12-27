import pytest
from Words import Word, Words
from Words import EmptyWordError, EmptyWordListError
from Wheel_of_fortune import Wheel_of_fortune
from Wheel_of_fortune import EmptyWheelOfFortuneError, Wheel_data
from Utilities import read_from_csv
from io import StringIO
import random


def test_create_word():
    word = Word('koło fortuny')
    assert word.word == 'koło fortuny'.upper()
    letters_list = ['K', 'O', 'Ł', 'O', 'F', 'O', 'R', 'T', 'U', 'N', 'Y']
    assert (letter in letters_list for letter in word.letters_dict)
    assert word.letter_repr() == '____ _______'
    starting_repr = word.letter_repr()
    new_word_repr = word.update_letter_repr(starting_repr, 'ł')
    assert new_word_repr == '__Ł_ _______'


def test_create_empty_word():
    with pytest.raises(EmptyWordError):
        Word('')


def test_create_Words_list():
    word1 = Word('gra')
    word2 = Word('koło')
    word3 = Word('fortuna')
    assert word1.word == 'GRA'
    letters_list1 = ['G', 'R', 'A']
    assert (letter in letters_list1 for letter in word1.letters_dict)
    assert word2.word == 'KOŁO'
    letters_list2 = ['K', 'O', 'Ł', 'O']
    assert (letter in letters_list2 for letter in word2.letters_dict)
    assert word3.word == 'FORTUNA'
    letters_list3 = ['F', 'O', 'R', 'T', 'U', 'N', 'A']
    assert (letter in letters_list3 for letter in word3.letters_dict)

    words = Words([word1, word2, word3])
    assert words.words == [word1, word2, word3]
    assert words.draw_word() in [word1, word2, word3]


def test_create_empty_Words_list():
    with pytest.raises(EmptyWordListError):
        Words([])


def test_read_from_csv():
    fh = StringIO('key,value\nmoney,150\nsurprise,NAGRODA\n')
    values_list = read_from_csv(fh)
    assert len(values_list) == 2
    assert values_list[1][0] == 'surprise'
    assert values_list[1][1].word == 'NAGRODA'


def test_create_wheel_of_fortune():
    fh = StringIO('key,value\nmoney,150\nsurprise,NAGRODA\n')
    values_list = read_from_csv(fh)
    wheel = Wheel_of_fortune(values_list)
    assert wheel.spin_wheel() in wheel.values


def test_create_empty_wheel_of_fortune():
    with pytest.raises(EmptyWheelOfFortuneError):
        Wheel_of_fortune()
