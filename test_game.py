import pytest
from Words import Word, Words
from Words import EmptyWordError, EmptyWordListError, InvalidLetterValueError


def test_create_word():
    word = Word('koło fortuny')
    assert word.word == 'koło fortuny'
    letters_list = ['k', 'o', 'ł', 'o', 'f', 'o', 'r', 't', 'u', 'n', 'y']
    assert word.letters_list == letters_list
    assert word.letter_representation() == '____ _______'
    starting_repr = word.letter_representation()
    new_word_repr = word.update_letter_representation(starting_repr, 'ł')
    assert new_word_repr == '__ł_ _______'


def test_create_empty_word():
    with pytest.raises(EmptyWordError):
        Word('')


def test_create_Words_list():
    word1 = Word('gra')
    word2 = Word('koło')
    word3 = Word('fortuna')
    assert word1.word == 'gra'
    letters_list1 = ['g', 'r', 'a']
    assert word1.letters_list == letters_list1
    assert word2.word == 'koło'
    letters_list2 = ['k', 'o', 'ł', 'o']
    assert word2.letters_list == letters_list2
    assert word3.word == 'fortuna'
    letters_list3 = ['f', 'o', 'r', 't', 'u', 'n', 'a']
    assert word3.letters_list == letters_list3

    words = Words([word1, word2, word3])
    assert words.words == [word1, word2, word3]
    assert words.random_choice() in [word1, word2, word3]


def test_create_empty_Words_list():
    with pytest.raises(EmptyWordListError):
        Words([])
