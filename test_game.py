from Words import Word
from Words import EmptyWordError, WordNotGivenError
from Wheel_of_fortune import Wheel_of_fortune
from Wheel_of_fortune import EmptyWheelOfFortuneError
from player import Player
from Utilities import read_from_csv
from database import Database, FilePathNotFound
from game import GameConfiguration, GameRound, Final
from Words import VOCALS, CONSONANTS
from io import StringIO
import random
import pytest


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
    assert word.category == 'NO CATEGORY'
    letters_list = ['K', 'O', 'Ł', 'O', 'F', 'O', 'R', 'T', 'U', 'N', 'Y']
    assert (letter in letters_list for letter in word.word)
    starting_repr = word.word_repr()
    assert starting_repr == '____ _______'
    new_word_repr = word.word_repr(['Ł'])
    assert new_word_repr == '__Ł_ _______'


def test_create_empty_word():
    with pytest.raises(EmptyWordError):
        Word('')
    with pytest.raises(EmptyWordError):
        Word('', 'nicość')
    with pytest.raises(WordNotGivenError):
        Word()


def test_create_Words_list():
    word1 = Word('gra')
    word2 = Word('koło', 'figura')
    word3 = Word('fortuna')
    assert word1.word == 'GRA'
    assert word1.category == 'NO CATEGORY'
    letters_list1 = ['G', 'R', 'A']
    assert (letter in letters_list1 for letter in word1.word)
    assert word2.word == 'KOŁO'
    assert word2.category == 'FIGURA'
    letters_list2 = ['K', 'O', 'Ł', 'O']
    assert (letter in letters_list2 for letter in word2.word)
    assert word3.word == 'FORTUNA'
    assert word3.category == 'NO CATEGORY'
    letters_list3 = ['F', 'O', 'R', 'T', 'U', 'N', 'A']
    assert (letter in letters_list3 for letter in word3.word)


def test_read_from_csv():
    fh = StringIO('key,value\nmoney,150\nsurprise,NAGRODA\n')
    values_list = read_from_csv(fh)
    assert len(values_list) == 2
    assert values_list[1].category == 'surprise'.upper()
    assert values_list[1].word == 'NAGRODA'


# # ???
# def test_read_from_json():
#     fh = StringIO("[{'key': 'money', 'value': 500}, {'value': 'BANKRUT'}]")
#     values_list = read_from_json(fh)
#     assert len(values_list) == 4
#     assert values_list[1].category == 'MONEY'
#     assert values_list[1].word == '500'
#     # assert values_list[3].category == 'NO CATEGORY'
#     # assert values_list[3].word == 'BANKRUT'


def test_database():
    path = 'values.txt'
    wordlist = Database().load_from_file(path)
    assert wordlist
    values = [word.word for word in wordlist]
    assert '500' in values


def test_database_errors():
    path = 'aaa/bb/c.txt'
    with pytest.raises(FilePathNotFound):
        Database().load_from_file(path)
    # don't have any directory in repo to test it

    # path = 'aaa/bb/c'
    # with pytest.raises(FilePathIsDirectory):
    #     Database().load_from_file(path)


def test_create_wheel_of_fortune():
    fh = StringIO('key,value\nmoney,150\nsurprise,NAGRODA\n')
    values_list = read_from_csv(fh)
    wheel = Wheel_of_fortune(values_list)
    assert wheel.spin_wheel() in wheel.values


def test_spin_wheel():
    fh = StringIO('value\n150\nNAGRODA\n')
    values_list = ['150', 'NAGRODA']
    values = read_from_csv(fh)
    wheel = Wheel_of_fortune(values)
    assert wheel.spin_wheel().word in values_list


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
    for reward in player.reward():
        assert reward in rewards


def test_player_total_balance():
    player = Player(1)
    assert player.id == 1
    assert player.balance() == 0
    player.add_to_balance(500)
    assert player.balance() == 500
    player.add_to_total_balance(player.balance())
    player.set_balance(0)
    assert player.balance() == 0
    assert player.total_balance() == 500


def test_clear_players_rewards_list():
    rewards = ['książka kucharska', 'telefon', 'cukierki']
    player = Player(1)
    assert not player.reward()
    player.add_reward(random.choice(rewards))
    player.add_reward(random.choice(rewards))
    assert player.reward().pop() in rewards
    assert player.reward()
    player.clear_reward()
    assert not player.reward()


# tests work only when words.txt file is in repo
def test_game_configuration_create_players():
    game_config = GameConfiguration('words.txt', 3)
    players = game_config.create_players()
    assert len(players) == 3
    id = 1
    for player in players:
        assert player.id == id
        id += 1


def test_game_configuration_get_word():
    game_config = GameConfiguration('words.txt', 3)
    assert game_config.get_word() not in game_config.words()


def test_create_game_round():
    values = ['100', '150', '200', '250', '300', '350', '400', '500', '550',
              'ZEGAREK', 'VOUCHER', 'BIŻUTERIA', 'BANKRUT', 'STOP']
    fh = StringIO('value\n100\n150\n200\n250\n300\n350\n400\n500\n550\n'
                  'ZEGAREK\nVOUCHER\nBIŻUTERIA\nBANKRUT\nSTOP')
    wheel = Wheel_of_fortune(read_from_csv(fh))
    for word in wheel.values:
        assert word.word in values
    player1 = Player(1)
    player2 = Player(2)
    players = [player1, player2]
    word = Word('porsche 911', 'auto')
    player_pointer = 1
    game_round = GameRound(players, word, wheel, player_pointer)
    assert player1, player2 in game_round.players
    for player in game_round._players:
        assert player.balance() == 0
        assert player.total_balance() == 0
        assert not player.reward()
    assert game_round._word_object.word == 'PORSCHE 911'
    assert game_round._word_object.category == 'AUTO'
    assert not game_round.letter_guesses
    consonants = {'P': 1, 'R': 1, 'S': 1, 'C': 1, 'H': 1}
    assert game_round.word_consonants == consonants
    assert game_round.word_repr == '_______ 911'


def test_game_round_update_word_repr():
    fh = StringIO('value\n100\n150\n200\n250\n300\n350\n400\n500\n550\n'
                  'ZEGAREK\nVOUCHER\nZESTAW GARNKÓW\nBIŻUTERIA\nBANKRUT\nSTOP')
    wheel = Wheel_of_fortune(read_from_csv(fh))
    player1 = Player(1)
    player2 = Player(2)
    players = [player1, player2]
    word = Word('porsche 911', 'auto')
    player_pointer = 1
    game_round = GameRound(players, word, wheel, player_pointer)
    game_round.word_repr = game_round._word_object.word_repr(['P', 'S', 'E'])
    assert game_round.word_repr == 'P__S__E 911'


def test_create_final():
    player1 = Player(1)
    player2 = Player(2)
    players = [player1, player2]
    word = Word('porsche 911', 'auto')
    final = Final(players, word)
    for letter in final.drawn_letters:
        assert letter in (VOCALS + CONSONANTS)


def test_final_find_best_player():
    player1 = Player(1)
    player2 = Player(2)
    players = [player1, player2]
    word = Word('porsche 911', 'auto')
    final = Final(players, word)
    assert final.find_best_player() is None
    final._players[1].add_to_total_balance(500)
    assert final.find_best_player() == player2
    final._players[0].add_to_total_balance(500)
    player1.add_reward('ZEGAREK')
    assert final.find_best_player() == player1
    final._players[1].add_reward('PRALKA')
    assert final.find_best_player() is None
