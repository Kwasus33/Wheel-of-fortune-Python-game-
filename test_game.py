from Words import Word
from Words import EmptyWordError, WordNotGivenError
from Wheel_of_fortune import Wheel_of_fortune
from Wheel_of_fortune import EmptyWheelOfFortuneError
from player import Player
from Utilities import read_from_csv
from database import Database, FilePathNotFound
from game import GameConfiguration, GameRound, Final
from settings import choose_game_mode, prepare_game, give_file_path
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
    player.remove_rewards()
    assert not player.reward()


def test_choose_game_mode(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda answer: 1)
    answer = choose_game_mode()
    assert answer == '1'
    inputs = iter([4, 2])
    monkeypatch.setattr('builtins.input', lambda answer: next(inputs))
    answer = choose_game_mode()
    assert answer == '2'


def test_prepare_game_out_of_range_game_mode():
    with pytest.raises(Exception):
        prepare_game('4')


def test_give_file_path(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda path: 'words.txt')
    answer = give_file_path(3)
    assert answer == 'words.txt'


def test_game_configuration_create_default_wheel_of_fortune(monkeypatch):
    values = ['100', '150', '200', '250', '300', '350', '400', '500', '550',
              'ZEGAREK', 'VOUCHER', 'BIŻUTERIA', 'BANKRUT', 'STOP']
    game_config = GameConfiguration('words.txt', 3)
    monkeypatch.setattr('builtins.input', lambda answer: '')
    wheel = game_config.choose_wheel_of_fortune()
    assert wheel.spin_wheel().word in values


def test_game_configuration_create_own_wheel_of_fortune(monkeypatch):
    values = ['100', '150', '200', '250', '300', '350', '400', '500', '550',
              'ZEGAREK', 'VOUCHER', 'BIŻUTERIA', 'BANKRUT', 'STOP']
    game_config = GameConfiguration('words.txt', 3)
    inputs = iter(['t', 'values.txt'])
    monkeypatch.setattr('builtins.input', lambda answer: next(inputs))
    wheel = game_config.choose_wheel_of_fortune()
    assert wheel.spin_wheel().word in values


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


def create_game_round():
    """
    Func creating GameRound class object, it is used in a few tests
    """
    fh = StringIO('value\n100\n150\n200\n250\n300\n350\n400\n500\n550\n'
                  'ZEGAREK\nVOUCHER\nBIŻUTERIA\nBANKRUT\nSTOP')
    wheel = Wheel_of_fortune(read_from_csv(fh))
    player1 = Player(1)
    player2 = Player(2)
    players = [player1, player2]
    word = Word('porsche 911', 'auto')
    player_pointer = 1
    return GameRound(players, word, wheel, player_pointer)


def test_create_game_round():
    values = ['100', '150', '200', '250', '300', '350', '400', '500', '550',
              'ZEGAREK', 'VOUCHER', 'BIŻUTERIA', 'BANKRUT', 'STOP']
    game_round = create_game_round()
    for word in game_round.wheel.values:
        assert word.word in values
    for player in game_round._players:
        assert player.balance() == 0
        assert player.total_balance() == 0
        assert not player.reward()
    assert game_round._word_object.word == 'PORSCHE 911'
    assert game_round._word_object.category == 'AUTO'
    assert not game_round.letter_guesses()
    consonants = {'P': 1, 'R': 1, 'S': 1, 'C': 1, 'H': 1}
    assert game_round.word_consonants() == consonants
    assert game_round.word_repr == '_______ 911'


def test_game_round_update_word_repr():
    game_round = create_game_round()
    game_round.word_repr = game_round._word_object.word_repr(['P', 'S', 'E'])
    assert game_round.word_repr == 'P__S__E 911'


def test_game_round_read_letter(monkeypatch):
    game_round = create_game_round()
    inputs = iter(['a', 'e', 'b'])
    monkeypatch.setattr('builtins.input', lambda letter: next(inputs))
    letter = game_round.read_letter(None)
    assert letter == 'A'
    letter = game_round.read_letter('150')
    assert letter == 'B'


def test_game_round_guess_correct_letter_win_money(monkeypatch):
    game_round = create_game_round()
    player1 = game_round.players[0]
    monkeypatch.setattr('builtins.input', lambda letter: 'r')
    is_good_guess = game_round.guess_letter(player1, '300')
    assert is_good_guess
    assert game_round.word_repr == '__R____ 911'
    assert game_round.word_consonants() == {'P': 1, 'S': 1, 'C': 1, 'H': 1}
    assert game_round.letter_guesses() == ['R']
    assert player1.balance() == 300
    monkeypatch.setattr('builtins.input', lambda letter: 'e')
    is_good_guess = game_round.guess_letter(player1)
    assert is_good_guess
    assert game_round.word_repr == '__R___E 911'
    assert game_round.word_consonants() == {'P': 1, 'S': 1, 'C': 1, 'H': 1}
    assert game_round.letter_guesses() == ['R', 'E']


def test_game_round_guess_correct_letter_get_reward(monkeypatch):
    game_round = create_game_round()
    player1 = game_round.players[0]
    monkeypatch.setattr('builtins.input', lambda letter: 's')
    is_good_guess = game_round.guess_letter(player1, 'ZEGAREK')
    assert is_good_guess
    assert game_round.word_repr == '___S___ 911'
    assert game_round.word_consonants() == {'P': 1, 'R': 1, 'C': 1, 'H': 1}
    assert game_round.letter_guesses() == ['S']
    assert 'ZEGAREK' in player1.reward()
    assert player1.balance() == 0


def test_game_round_guess_incorrect_letter(monkeypatch):
    game_round = create_game_round()
    player1 = game_round.players[0]
    monkeypatch.setattr('builtins.input', lambda letter: 'w')
    is_good_guess = game_round.guess_letter(player1, '300')
    assert not is_good_guess
    assert game_round.word_repr == '_______ 911'
    assert game_round.word_consonants() == {'P': 1, 'R': 1, 'S': 1,
                                            'C': 1, 'H': 1}
    assert game_round.letter_guesses() == ['W']


def test_game_round_guess_word_correctly(monkeypatch):
    game_round = create_game_round()
    monkeypatch.setattr('builtins.input', lambda letter: 'porSchE 911')
    is_good_guess = game_round.guess_word()
    assert is_good_guess
    assert game_round.word_repr == 'PORSCHE 911'
    assert game_round.word_consonants() == {}


def test_game_round_guess_word_incorrectly(monkeypatch):
    game_round = create_game_round()
    monkeypatch.setattr('builtins.input', lambda letter: 'bugatti 911')
    is_good_guess = game_round.guess_word()
    assert not is_good_guess
    assert game_round.word_repr == '_______ 911'
    assert game_round.word_consonants() == {'P': 1, 'R': 1, 'S': 1,
                                            'C': 1, 'H': 1}


def test_game_round_buy_vocal(monkeypatch):
    game_round = create_game_round()
    player1 = game_round.players[0]
    player1.set_balance(300)
    assert player1.balance() == 300
    monkeypatch.setattr('builtins.input', lambda letter: 'e')
    is_good_guess = game_round.buy_vocal(player1)
    assert player1.balance() == 100
    assert is_good_guess
    assert game_round.word_repr == '______E 911'
    assert game_round.word_consonants() == {'P': 1, 'R': 1, 'S': 1,
                                            'C': 1, 'H': 1}
    assert game_round.letter_guesses() == ['E']


def test_game_round_choose_action(monkeypatch):
    game_round = create_game_round()
    player1 = game_round.players[0]
    assert game_round.word_consonants() == {'P': 1, 'R': 1, 'S': 1,
                                            'C': 1, 'H': 1}
    inputs = iter(['B', 'S'])
    monkeypatch.setattr('builtins.input', lambda letter: next(inputs))
    answer = game_round.choose_action(player1)
    assert answer == 'S'
    player1.set_balance(500)
    monkeypatch.setattr('builtins.input', lambda letter: 'b')
    answer = game_round.choose_action(player1)
    assert answer == 'B'


def test_game_round_win_money(monkeypatch):
    game_round = create_game_round()
    player2 = game_round.players[1]
    inputs = iter(['r', 'b', 'e', 's'])
    monkeypatch.setattr('builtins.input', lambda letter: next(inputs))
    is_good_guess = game_round.win_money('300', player2)
    assert is_good_guess
    assert game_round.word_repr == '__R___E 911'
    assert game_round.word_consonants() == {'P': 1, 'S': 1, 'C': 1, 'H': 1}
    assert game_round.letter_guesses() == ['R', 'E']
    assert player2.id == 2
    assert player2.balance() == 100


def create_final():
    player1 = Player(1)
    player2 = Player(2)
    players = [player1, player2]
    word = Word('porsche 911', 'auto')
    return Final(players, word)


def test_create_final():
    final = create_final()
    for letter in final.drawn_letters:
        assert letter in (VOCALS + CONSONANTS)


def test_final_find_best_player():
    final = create_final()
    player1, player2 = final._players
    assert final.find_best_player() is None
    final._players[1].add_to_total_balance(500)
    assert final.find_best_player() == player2
    final._players[0].add_to_total_balance(500)
    player1.add_reward('ZEGAREK')
    assert final.find_best_player() == player1
    final._players[1].add_reward('PRALKA')
    assert final.find_best_player() is None


def test_final_choose_letters_set_with_mistakes(monkeypatch):
    final = create_final()
    drawn_letters = [letter for letter in final.drawn_letters]
    inputs = iter(['r', 'b', 'e', 's', 'a'])
    monkeypatch.setattr('builtins.input', lambda letter: next(inputs))
    final.choose_letters_set()
    assert drawn_letters + ['R', 'B', 'S', 'A'] == final.drawn_letters
