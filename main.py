#!/bin/python3
# -*- coding: utf-8 -*-
import random
import time
from datetime import date
import tools as t

for i in ["csv1.csv", "csv2.csv", "inserts.sql","update.sql"]:
    t.clearfile(i)

FIRST_NAME_LIST = 'Imionam.txt'
FIRST_NAME_LIST_SIZE = t.size_of_list(FIRST_NAME_LIST)
LAST_NAME_LIST = 'nazwiska.txt'
LAST_NAME_LIST_SIZE = t.size_of_list(LAST_NAME_LIST)
CAR_MAKE_LIST = 'samochody.txt'
CAR_MAKE_LIST_SIZE = t.size_of_list(CAR_MAKE_LIST)
CAR_MODEL_LIST = 'modele.txt'
CAR_MODEL_LIST_SIZE = t.size_of_list(CAR_MODEL_LIST)
cities=["Gdańsk","Gdynia","Wrocław","Poznań","Straszyn","Sopot","Pruszcz Gdański"]
streets=["ul. Długa","ul. Szeroka","ul. Konwaliowa","ul. Focha","ul. Jaworowa","ul. Lipowa","ul. Dębowa","ul. Leśna Góra"]
sources=["Od znajomego", "Przez reklamę na Facebooku", "Przez reklamę na innym portalu", "Przez reklamę tradycyjną", "Inne"]

LICZBA_DYSPOZYTOROW = 10#int(input('Podaj liczbę dyspozytorow: '))
LICZBA_KIEROWCOW = 20#int(input('Prodaj liczbe kierowcow: '))
LICZBA_KLIENTOW = 40#int(input('Podaj liczbe klientow: '))
LICZBA_SAMOCHODOW = 25#int(input('Podaj liczbe samochodow: '))
LICZBA_APLIKACJI = 24#int(input('Podaj liczbe aplikacji: '))
assert LICZBA_APLIKACJI <= LICZBA_KLIENTOW
LICZBA_KART = 10#int(input('Podaj liczbe kart platniczych: '))
LICZBA_WYKORZYSTAN = 26#int(input('Podaj liczbe wykorzystan: '))
LICZBA_PRZEJAZDOW = 45#int(input('Podaj liczbe przejazdow: '))

dyspozytornie = [t.Dyspozytornie('Gdańsk'), t.Dyspozytornie('Wrocław'), t.Dyspozytornie('Poznań')]
dyspozytorzy = []
samochody=[]
kierowcy=[]
klienci=[]
aplikacje=[]
karty=[]
wykorzystania=[]
przejazdy=[]
current_pesel = '7010110332'


def generuj_przejazdy(liczba):
    generuj_przejazdy.nr_faktury = 1
    for i in range(liczba):
        faktura = random.choice(["null","null","null",generuj_przejazdy.nr_faktury])
        if faktura!="null":
            generuj_przejazdy.nr_faktury+=1
        wykorzystanie = random.choice(wykorzystania)
        date = t.get_random_date(wykorzystanie.args[3][1], wykorzystanie.args[4][1])
        ocena = random.randint(1, 5)
        poczatek_ulica = random.choice(streets)
        poczatek_nrdomu = random.randint(1, 200)
        poczatek_miasto = random.choice(cities)
        koniec_ulica = random.choice(streets)
        koniec_nrdomu = random.randint(1, 200)
        koniec_miasto = poczatek_miasto
        koszt = random.randint(15, 50)
        napiwek = random.randint(0, 20)
        czas = random.randint(1, 60)
        godzina = str(random.randint(0, 23)).zfill(2) + ':' + str(random.randint(0, 59)).zfill(2) + ':' + str(
            random.randint(0, 59)).zfill(2)
        fk_klienci = random.choice(klienci)
        fk_kierowcy = wykorzystanie.args[2][1]
        fk_dyspozytorzy = random.choice(dyspozytorzy)
        fk_samochody = wykorzystanie.args[1][1]
        print(fk_samochody)
        przejazdy.append(t.Przejazdy(date, i, ocena, poczatek_ulica, poczatek_nrdomu, poczatek_miasto,
                                     koniec_ulica, koniec_nrdomu, koniec_miasto, koszt, napiwek, czas, godzina, faktura,
                                     fk_klienci.args[fk_klienci.primary_key][1], fk_kierowcy,
                                     fk_dyspozytorzy.args[fk_dyspozytorzy.primary_key][1],
                                     fk_samochody))


for i in range(LICZBA_DYSPOZYTOROW):
    fname = t.take_random_line(FIRST_NAME_LIST, FIRST_NAME_LIST_SIZE)
    lname = t.take_random_line(LAST_NAME_LIST, LAST_NAME_LIST_SIZE)
    dyspozytornia = dyspozytornie[t.randint(0, 2)]
    fk_dyspozytornie = dyspozytornia.args[dyspozytornia.primary_key][1]
    dyspozytorzy.append(t.Dyspozytorzy(fname, lname, current_pesel + '4', fk_dyspozytornie))
    current_pesel = t.generate_pesel(current_pesel)

for i in range(LICZBA_SAMOCHODOW):
    make=t.take_random_line(CAR_MAKE_LIST,CAR_MAKE_LIST_SIZE)
    model = t.take_random_line(CAR_MODEL_LIST,CAR_MODEL_LIST_SIZE)
    year= random.randint(1991, 2017);
    ID=random.choice(["GD","PO","DW","GA"])+str(random.randint(10000,99999))
    data_przegladu=random.randint(2007,2017)
    ours=random.choice([True,False])
    samochody.append(t.Samochody(ID,data_przegladu,make,model,year,ours))

for i in range(LICZBA_KIEROWCOW):
    fname = t.take_random_line(FIRST_NAME_LIST, FIRST_NAME_LIST_SIZE)
    lname = t.take_random_line(LAST_NAME_LIST, LAST_NAME_LIST_SIZE)
    current_pesel = t.generate_pesel(current_pesel)
    registration_date=t.get_random_date()
    kierowcy.append(t.Kierowcy(fname,lname,current_pesel,registration_date))

for i in range(LICZBA_KLIENTOW):
    fname = t.take_random_line(FIRST_NAME_LIST, FIRST_NAME_LIST_SIZE)
    lname = t.take_random_line(LAST_NAME_LIST, LAST_NAME_LIST_SIZE)
    phone = random.randint(500000000,699999999)
    klienci.append(t.Klienci(fname,lname,phone,i))

klienci_copy = list(klienci)
for i in range(LICZBA_APLIKACJI):
    city = random.choice(cities)
    street=random.choice(streets)
    house=random.randint(1,200)
    zrodlo=random.choice(sources)
    registration_date = t.get_random_date()
    fk_klienci = klienci_copy.pop()
    aplikacje.append(t.Aplikacje(street,house,city,zrodlo,registration_date,fk_klienci.args[fk_klienci.primary_key][1]))

for i in range(LICZBA_KART):
    number = random.randint(1000000000000000,9999999999999999)
    security= random.randint(100,999)
    fk_klienci = random.choice([x.args[x.primary_key][1] for x in aplikacje])
    karty.append(t.Karty(number,security,fk_klienci))

for i in range(LICZBA_WYKORZYSTAN):
    nr = random.choice([samochod.args[samochod.primary_key][1] for samochod in samochody])
    pesel = random.choice([x.args[x.primary_key][1] for x in kierowcy])
    data_rozpoczecia=t.get_random_date(date(2016,6,30))
    data_zakonczenia=t.get_random_date(data_rozpoczecia)
    wykorzystania.append(t.Wykorzystania(i,nr,pesel,data_rozpoczecia,data_zakonczenia))


generuj_przejazdy(LICZBA_PRZEJAZDOW)

for e in dyspozytornie:
    e.to_sql('inserts.sql')

for e in dyspozytorzy:
    e.to_sql('inserts.sql')

for e in kierowcy:
    e.to_sql('inserts.sql')

for e in klienci:
    e.to_sql('inserts.sql')

for e in aplikacje:
    e.to_sql('inserts.sql')

for e in karty:
    e.to_sql('inserts.sql')

for e in przejazdy:
    e.to_sql('inserts.sql')

for e in samochody:
    e.to_csv('csv1.csv')

for e in wykorzystania:
    e.to_csv('csv2.csv')


"""
drugi punkt w czasie
"""

NOWE_PRZEJAZDY = 30
NOWE_TELEFONY_KLIENTÓW = 10
generuj_przejazdy(NOWE_PRZEJAZDY)


for i in range(NOWE_TELEFONY_KLIENTÓW):
    random.choice(klienci).update('update.sql', 2, random.randint(500000000,699999999))
