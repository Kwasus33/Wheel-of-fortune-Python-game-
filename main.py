from settings import choose_game_mode
from settings import training_game_mode, standard_game_mode, custom_game_mode


def main():

    game_mode = choose_game_mode()

    if game_mode == '1':
        training_game_mode()
    elif game_mode == '2':
        standard_game_mode()
    else:
        custom_game_mode()


if __name__ == "__main__":
    main()


# Z R O B I O N E
    # czy potrzebny jest warunek dający znać i uniemożliwiający
    # wybór opcji buy kiedy w słowie skończą się samogłoski

    # NAPRAWIONE - prosty kod uniemożliwiający to dla spółgłosek
    # DO PRZEMYŚLENIA - samogłoski można podać wiele razy te same,
    # za każdym razem gracz traci pieniądze a reprezentacja się nie zmienia
    # NAPRAWA - dodając tablicę z odgadniętymi przez osoby literami
    # i warunek szukania słowa póki '_' są w słowie można to łatwo naprawić

    # gdy w zgadywanym słowie poda się drugi raz do odgadnięcia
    # literę już odganiętą to
    # amount = self.word_consonants[letter] * int(value)
    # w funkcji guess_letter() wyrzuca key error
    # bo litera została już usunięta z tablicy
    # trzeba dodać tablicę z odganiętymi literami

    # w finale po upływie 20 sekund dalej trzeba podać jakąś wartość do inputa
    # a powinna kończyć się funkcja z info o przegranej
    # mechanizm znajdywania najlepszego gracza jest słaby i nie działa git


# D O   Z R O B I E N I A

    # !!!
    # gdy nie ma już spółgłosek a gracza nie stać na kupienie samogłoski
    # powinien albo od razu dostać komunikat i nie mieć tej opcji albo po
    # pierwszej próbie zakupu, dostać info i nie móc wybrać opcji zakupu (B)
    # !!!

    # uproszczenie niektórych funkcji
    # ewentualna optymalizacja kodu - jeśli znajdę na to pomysł
    # poprawki stylistyczne wyświetlanych w terminalu komunikatów
    # warunek sprawdzający żeby plik z hasłami miał {liczba rund + finał} haseł

    # E W E N T U A L N I E
    #   mogę dodać sprawdzenie żeby użytkownik nie mógł podać w finale
    #   liter które już zostały dla niego wylosowane lub sam podał -
    #   nie dodałem tego warunku - można zwielokrotnić podane litery


# I N F O / P R Z Y P O M I N A J K A
    # zanim skończą się litery alfabetu do wyboru w zgadywaniu
    # to najpierw skończą się litery w słowie odgadywanym
    # maksymalnie słowo może zawierać wszytskie litery alfabetu
    # znaki nie będące literami są wyświetlane w reprezentacji hasła
    # więc nie ma możliwości wyjścia poza zakres
