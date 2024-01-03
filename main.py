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


# D O   Z R O B I E N I A

    # ZROBIONE WYRZUCANIE BŁĘDU GDY PLIK JEST ZA KRÓTKI:
    # warunek sprawdzający żeby plik z hasłami miał {liczba rund + finał} haseł

    # poprawki stylistyczne wyświetlanych w terminalu komunikatów

    # E W E N T U A L N I E
    #   mogę dodać sprawdzenie żeby użytkownik nie mógł podać w finale
    #   liter które już zostały dla niego wylosowane lub sam podał -
    #   nie dodałem tego warunku - można zwielokrotnić podane litery


# I N F O / P R Z Y P O M I N A J K A
    # RACZEJ NIE
    #   czy potrzebny jest warunek dający znać i uniemożliwiający
    #   wybór opcji buy kiedy w słowie skończą się samogłoski

    # zanim skończą się litery alfabetu do wyboru w zgadywaniu
    # to najpierw skończą się litery w słowie odgadywanym
    # maksymalnie słowo może zawierać wszytskie litery alfabetu
    # znaki nie będące literami są wyświetlane w reprezentacji hasła
    # więc nie ma możliwości wyjścia poza zakres
