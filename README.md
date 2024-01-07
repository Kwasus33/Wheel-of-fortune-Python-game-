# PROJEKT PIPR - KOŁO FORTUNY

## DANE AUTORA:
* JAKUB KWAŚNIAK
* NR INDEKSU: 331396


## POLECENIE:

Celem projektu jest zaimplementowanie gry "Koło fortuny". Gra składa się z trzech rund zasadniczych i finału.

W każdej rundzie odgadywane jest hasło wylosowane spośród bazy haseł wczytywanej z pliku. Uczestnicy widzą kategorię z jakiej pochodzi hasło oraz zamaskowany układ liter. Uczestnik "kręci kołem" czym losuje kwotę punktową lub nagrodę specjalną (utrata kolejki, bankrut, nagroda rzeczowa). Następnie odgaduje spółgłoskę. Za każdą trafioną literę otrzymuje wylosowaną kwotę punktową a trafione litery w haśle są odsłaniane, po czym gracz może:

* zakręcić ponownie kołem,
* kupić samogłoskę,
* odgadnąć hasło.

Jeżeli gracz nie trafi żadnej litery, kolejka przechodzi na kolejnego gracza.

W rundzie finałowej gracz, który w ciągu trzech rund zdobył największą liczbę punktów, odgaduje hasło finałowe. Losowane jest 5 liter, do których gracz może dołożyć cztery kolejne. Po odsłonięciu trafień gracz ma kilka sekund na odgadnięcie hasła finałowego. Jak mu się to uda, to wygrywa Poloneza.

Interfejs gry może być tekstowy lub graficzny. W przypadku interfejsu tekstowego można się pobawić znakami sterującymi, które czyszczą ekran terminala.

## PODZIAŁ PROGRAMU I OPIS KLAS

### game.py
* Klasa GameConfiguration
    * odpowiada za przygotowanie obiektów potrzebnych w rozgrywce - rundach zasadniczych oraz finale
    * przygotowuje liste haseł, losowanych w rundach zasadniczych oraz finale, pobiera je z pliku do którego ścieżkę podaje użytkownik
    * tworzy graczy biorących udział w rozgrywce
    * przygotowuje koło fortuny z wartościami, losowanymi w rundach zasadniczych przez graczy, pobiera wartości z pliku, gracze mogą podać ścieżkę do własnego pliku z wartościami lub wybrać przygotowane wartości standardowe
    * losuje hasło z przygotowanej listy haseł oraz usuwa je z niej by wylosowane hasła się nie powtarzały

* Klasa GameRound
    * jest reprezentacją pojedyńczej rundy w rozgrywce
    * pozwala graczom kręcić kołem fortuny, odgadywać spółgłoski i zdobywać wylosowane kwoty punktowe/nagrody, po odgadnięciu poprawnej spółgłoski gracz może zakręcić ponownie kołem, odgadnąć hasło lub kupić samogłoskę, jeżeli ma zdobytą min. 200 kwotę punktową. Gracze mogą kręcić kołem fortuny dopóki w wylosowanym słowie znajdują się nieodgadnięte spółgłoski
    * gdy wszystkie spółgłoski zostaną odgadnięte, gracze może odgadnąć hasło lub kupić samogłoskę, jeżeli ma na koncie min. 200 (zdobyta kwota punktowa)
    * w przypadku wylosowania STOP kręcąc kołem, niepoprawnego odgadnięcia hasła lub spółgłoski, kupienia samogłoski nieznajdującej się w odgadywanym haśle gracz traci kolejkę, w przypadku wylosowania BANKRUT kręcąc kołem fortuny gracz traci kolejkę oraz jego zdobyta kwota punktowa jest zerowana
    * gracz który odganie hasło (poda poprawne hasło lub wylosuje odgadnie ostatnią brakującą spółgłoskę lub kupi ostatnią brakującą samogłoskę) wygrywa rundę, wygrany zachowuje zdobytą kwotę punktową oraz nagrody, konta pozostałych graczy są zerowane a listy nagród czyszczone

* Klasa Final
    * jest reprezentacją rundy finałowej
    * pozwala wybrać najlepszego z garczy, który weźmie udział w rundzie finałowej, wybiera garcza z najwyższą kwotą punktową, jeżeli jest więcej niż jeden taki gracz, wybiera gracza z największą liczbą zdobytych nagród, jeżeli jest kilku graczy z najwyższą kwotą punktową oraz liczbą zdobytych nagród, zwrócona zostaje informacja, że runda finałowa się nie odbędzie - nie da się wskazać najlepszego gracza
    * jeżeli da się wskazać najlepszego gracza, losowany jest dla niego zestaw 3 spółgłosek oraz 2 samogłosek, gracz wybiera 3 spółgłoski oraz 1 samogłoskę, po czym w haśle finałowym odsłaniane są wylosowane i wybrane przez gracza litery
    * od momentu odsłonięcia hasła gracz ma 20 sekund na podanie poprawnej odpowiedzi, jeżeli mu się to dostanie komuniakat o wygraniu poloneza, w przeciwnym wypadku o przegraniu finału

### player.py
* Klasa Player
    * służy do reprezentowania pojedyńczego gracza
    * obiekty tej klasy gromadzą informacje o identyfikatorze gracza, zdobytych nagrodach i kwotach punktowych w trakcie rund oraz o zatrzymanych nagrodach i kwotach punktowych w wyniku wygrania rundy

### Wheel_of_fortune.py
* Klasa Wheel_of_fortune
    * służy do reprezentacji koła fortuny, pozwala na "zakręcenie kołem fortuny" - wylosowanie wartości z listy wartośći koła, podanej przy tworeniu obiektu tej klasy

### Words.py
* Klasa Words
    * służy do reprezentacji słów - haseł do odgadnięcia podczas rund i finału gry oraz wartości podawanych przy tworzeniu obiektu klasy Wheel_of_fortune
    * przechowuje słowo oraz jego kategorię (jeśli jest podana), pozwala na otrzymanie zamaskowanego układu liter hasła z odsłniętymi już odgadniętymi literami

### settings.py
* znajdują się tu funkcje odpowiedzialne za wybór jednego z 3 dostępnych trybów gry oraz przeprowadzenie całej rozgrywki

### main.py
* użytownik wybiera jeden z trzech trybów gry, zostaje wywołana funkcja odpowiedzialna za całą rozgrywkę

### Utilities.py
* znajdują się tu funkcję odpwiedzialne za czytanie danych z plików, czyszcenie odpowiedzi podawanych przez graczy (w inputach) oraz danych czytanych z plików oraz czyszczenie okna terminala

## INSTRUKCJA UŻYTKOWNIKA
* W celu rozpoczęcia gry należy uruchomić plik main.py
* Po uruchomieniu programu należy wybrać jeden z 3 dostępnych trybów gry, tryb 2 to tryb standardowy (opisany w poleceniu) składający się z 3 rund zasadniczych oraz finału, rozgrywany przez 3 graczy (tak jak w telewizyjnym kole fortuny). Dodane zostały również 2 dodatkowe tryby - tryb 1 treningowy, składający się z 3 rund oraz finału rozgrywanych przez 1 gracza oraz tryb 3, konfigurowalny, w którym można wybrać od 2 do 6 graczy, a liczba rund jest taka jak liczba graczy
* Następnie należy podać ścieżkę do pliku zawierającego hasła do losowania w rozgrywce, zostanie wyświetlona minimalna liczba haseł wymaganych w pliku, jeżeli podany plik nie zawiera wymaganej liczby haseł zostanie wzniesiony wyjątek informujący, że podano scieżkę do niepoprawnego pliku, hasła w pliku mogą zawierać tylko polskie lub angielskie znaki (do testowania działania programu można wykorzystać znajdujący się w repozytorium plik 'words.txt' lub 'words.json')
* podawane pliki mogą być w formacie .txt (w konwencji csv) lub .json
* plik z hasłami powinien być sformatowany (przykład dla .txt, adekwatnie przygotować .jsona):
    key,value
    'auto','porsche'
    'potrawa','kotlet schabowy'
    ''
    ...
* gdzie value to słowo a key to kategoria słowa, obie wartości są wymagane, w przypadku braku jednej z nich zostanie wzniesiony wyjątek
* następnie należy wybrać czy wartości na kole fortuny mają być załadowane z własnego pliku czy z pliku z wartościami standardowymi (values.txt), w przypadku wybrania chęci podania ścieżki do pliku z własnymi wartościami,
* podawane pliki mogą być w formacie .txt lub .json
* należy podać plik sformatowany (przykład dla .txt, adekwatnie przygotować .jsona):
    value
    100
    300
    NAGRODA
    ZEGAREK
    BANKRUT
    STOP
* plik powinien zawierać pola BANKRUT, STOP, kwoty punktowe (np. 350, 500), nazwy nagród (np. ZESTAW GARNKÓW, VOUCHER)
* następnie rozpoczyna się rozgrywka, gracze powinni postępować zgodnie z wyświetlanymi komunikatami
* **Proszę nie usuwać, ani nie przenosić z repozytorium plików 'values.txt' oraz 'words.txt' - są to pliki odpowiednio konfiguracyjny i testowy**

## CZĘŚĆ REFLEKSYJNA
* udało się zaimplementować działającą grę 'koło-fortuny'
* względem pierwotnego pomysłu i polecenia zaimplementowane zostały 2 dodatkowe tryby gry oraz możliwość konfiguracji wartości koła fortuny, również zmodyfikowane zostały funkcje odpowiedzialne za reprezentacja losowanych haseł oraz poprawiona została stylistyka kodu (względem pierwszych wersji projektu)
* napotaknym problemem była analiza wszystkich warunków brzegowych w logice gry (np. sytuacje gdy kończą się samogłoski do kupienia a zostają spółgłoski do zgadnięcia czy gdy po wszystkich rundach zasadniczych jest więcej niż jeden najlepszy gracz) - co zmusiło mnie do wielokrotnej modyfikacji logiki
* wymagające było również zaimplementowanie przejrzystego wyświetlaniania komunikatów gry w terminalu
* nieststety nie udało się przygotować gui czy rozbudować rozgrywki o dodatkowe rundy (niewymagane w poleceniu), np. takie jak w telewizyjnym kole fortuny - powodem była niewystarczająca ilość czasu