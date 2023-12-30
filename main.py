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

    # NAPRAWIONE - prosty kod uniemożliwiający to dla spółgłosek
    # DO PRZEMYŚLENIA - samogłoski można podać wiele razy te same,
    # za każdym razem gracz traci pieniądze a reprezentacja się nie zmienia
    # NAPRAWA - dodając tablicę z odgadniętymi przez osoby literami
    # i warunek szukania słowa póki '_' są w słowie można to łatwo naprawić

    # gdy w zgadywanym słowie poda się drugi raz do odgadnięcia
    # literę już odganiętą to
    # amount = self.letters_to_guess[letter] * int(value)
    # w funkcji guess_letter() wyrzuca key error
    # bo litera została już usunięta z tablicy
    # trzeba dodać tablicę z odganiętymi literami

    # w finale po upływie 20 sekund dalej trzeba podać jakąś wartość do inputa
    # a powinna kończyć się funkcja z info o przegranej
    # mechanizm znajdywania najlepszego gracza jest słaby i nie działa git

    word = menu.get_word()
    final = Final(players, word)
    print(final.play_final())

    # mogę dodać sprawdzenie żeby użytkownik nie mógł podać w finale
    # liter które już zostały dla niego wylosowane lub sam podał


if __name__ == "__main__":
    main()
