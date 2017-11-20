import tools as t

FIRST_NAME_LIST = 'Imionam.txt'
FIRST_NAME_LIST_SIZE = t.size_of_list(FIRST_NAME_LIST)
LAST_NAME_LIST = 'nazwiska.txt'
LAST_NAME_LIST_SIZE = t.size_of_list(LAST_NAME_LIST)

LICZBA_DYSPOZYTOROW = int(input('Podaj liczbę dyspozytorow: '))
LICZBA_KIEROWCOW = int(input('Prodaj liczbe kierowcow: '))
LICZBA_KLIENTOW = int(input('Podaj liczbe klientow: '))
LICZBA_SAMOCHODOW = int(input('Podaj liczbe samochodow: '))
LICZBA_APLIKACJI = int(input('Podaj liczbe aplikacji: '))
LICZBA_KART = int(input('Podaj liczbe kart platniczych: '))
LICZBA_WYKORZYSTAN = int(input('Podaj liczbe wykorzystan: '))
LICZBA_PRZEJAZDOW = int(input('Podaj liczbe przejazdow: '))

dyspozytornie = [t.Dyspozytornie('Gdańsk'), t.Dyspozytornie('Wrocław'), t.Dyspozytornie('Poznań')]
dyspozytorzy = []
