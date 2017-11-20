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
current_pesel = '7010110332'

for i in range(LICZBA_DYSPOZYTOROW):
    fname = t.take_random_line(FIRST_NAME_LIST, FIRST_NAME_LIST_SIZE)
    lname = t.take_random_line(LAST_NAME_LIST, LAST_NAME_LIST_SIZE)
    dyspozytornia = dyspozytornie[t.randint(0, 2)]
    fk_dyspozytornie = dyspozytornia.args[dyspozytornia.primary_key]
    dyspozytorzy.append(t.Dyspozytorzy(fname, lname, current_pesel + '4', fk_dyspozytornie))
    current_pesel = t.generate_pesel(current_pesel)

for i in range(LICZBA_KART):
    pass#TODO