import pytest
from Words import Word, Words
from Words import EmptyWordError, WordNotGivenError, EmptyWordListError
from Wheel_of_fortune import Wheel_of_fortune
from Wheel_of_fortune import EmptyWheelOfFortuneError
from player import Player
from Utilities import read_from_csv
from io import StringIO
import random


def test_create_word():
    word = Word('koło fortuny', 'gra')
    assert word.word == 'koło fortuny'.upper()
    assert word.category == "GRA"
    letters_list = ['K', 'O', 'Ł', 'O', 'F', 'O', 'R', 'T', 'U', 'N', 'Y']
    assert (letter in letters_list for letter in word.word)
    assert word.word_repr() == '____ _______'
    assert word.word_repr(['Ł']) == '__Ł_ _______'


def test_create_word_without_category():
    word = Word('koło fortuny')
    assert word.word == 'koło fortuny'.upper()
    letters_list = ['K', 'O', 'Ł', 'O', 'F', 'O', 'R', 'T', 'U', 'N', 'Y']
    assert (letter in letters_list for letter in word.word)
    starting_repr = word.word_repr()
    assert starting_repr == '____ _______'
    new_word_repr = word.word_repr(['Ł'])
    assert new_word_repr == '__Ł_ _______'


def test_create_empty_word():
    with pytest.raises(EmptyWordError):
        Word('')
    with pytest.raises(WordNotGivenError):
        Word()


def test_create_Words_list():
    word1 = Word('gra')
    word2 = Word('koło')
    word3 = Word('fortuna')
    assert word1.word == 'GRA'
    letters_list1 = ['G', 'R', 'A']
    assert (letter in letters_list1 for letter in word1.word)
    assert word2.word == 'KOŁO'
    letters_list2 = ['K', 'O', 'Ł', 'O']
    assert (letter in letters_list2 for letter in word2.word)
    assert word3.word == 'FORTUNA'
    letters_list3 = ['F', 'O', 'R', 'T', 'U', 'N', 'A']
    assert (letter in letters_list3 for letter in word3.word)

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
    assert values_list[1].category == 'surprise'.upper()
    assert values_list[1].word == 'NAGRODA'


def test_create_wheel_of_fortune():
    fh = StringIO('key,value\nmoney,150\nsurprise,NAGRODA\n')
    values_list = read_from_csv(fh)
    wheel = Wheel_of_fortune(values_list)
    assert wheel.spin_wheel() in wheel.values


def test_create_empty_wheel_of_fortune():
    with pytest.raises(EmptyWheelOfFortuneError):
        Wheel_of_fortune()


def test_create_player():
    player = Player()
    assert player.id is None
    player2 = Player(2)
    assert player2.id == 2
    assert player.balance() == 0
    assert player2.balance() == 0
    player2.add_to_balance(500)
    player.add_to_balance(1)
    assert player.balance() == 1
    assert player2.balance() == 500
    player2.set_balance(10)
    assert player2.balance() == 10


def test_create_players():
    players = []
    for idx in range(3):
        players.append(Player(idx+1))
    assert players[0].id == 1
    assert players[1].id == 2
    assert players[2].id == 3


def test_set_players_reward():
    rewards = ['książka kucharska', 'telefon', 'cukierki']
    player = Player(1)
    assert not player.reward()
    player.add_reward(random.choice(rewards))
    player.add_reward(random.choice(rewards))
    for reward in player.rewards:
        assert reward in rewards
