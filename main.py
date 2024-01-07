from settings import choose_game_mode
from settings import prepare_game


def main():

    game_mode = choose_game_mode()
    prepare_game(game_mode)


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
