#!/bin/python3
# -*- coding: utf-8 -*-
import random
import time

from datetime import date

import tools as t

FIRST_NAME_LIST = 'Imionam.txt'
FIRST_NAME_LIST_SIZE = t.size_of_list(FIRST_NAME_LIST)
LAST_NAME_LIST = 'nazwiska.txt'
LAST_NAME_LIST_SIZE = t.size_of_list(LAST_NAME_LIST)
CAR_MAKE_LIST = 'samochody.txt'
CAR_MAKE_LIST_SIZE = t.size_of_list(CAR_MAKE_LIST)
CAR_MODEL_LIST = 'modele.txt'
CAR_MODEL_LIST_SIZE = t.size_of_list(CAR_MODEL_LIST)
cities=["Gdańsk","Gdynia","Wrocław","Poznań","Straszyn","Sopot","Pruszcz Gdański"]
streets=["ul. Długa","ul. Szeroka","ul. Konwaliowa","ul. Focha","ul. Jaworowa","ul. Lipowa","ul. Dębowa"]
sources=["Od znajomego", "Przez reklamę na Facebooku", "Przez reklamę na innym portalu", "Przez reklamę tradycyjną", "Inne"]

LICZBA_DYSPOZYTOROW = int(input('Podaj liczbę dyspozytorow: '))
LICZBA_KIEROWCOW = int(input('Prodaj liczbe kierowcow: '))
LICZBA_KLIENTOW = int(input('Podaj liczbe klientow: '))
LICZBA_SAMOCHODOW = int(input('Podaj liczbe samochodow: '))
LICZBA_APLIKACJI = int(input('Podaj liczbe aplikacji: '))
assert LICZBA_APLIKACJI <= LICZBA_KLIENTOW
LICZBA_KART = int(input('Podaj liczbe kart platniczych: '))
LICZBA_WYKORZYSTAN = int(input('Podaj liczbe wykorzystan: '))
LICZBA_PRZEJAZDOW = int(input('Podaj liczbe przejazdow: '))

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

for i in range(LICZBA_DYSPOZYTOROW):
    fname = t.take_random_line(FIRST_NAME_LIST, FIRST_NAME_LIST_SIZE)
    lname = t.take_random_line(LAST_NAME_LIST, LAST_NAME_LIST_SIZE)
    dyspozytornia = dyspozytornie[t.randint(0, 2)]
    fk_dyspozytornie = dyspozytornia.args[dyspozytornia.primary_key]
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
    aplikacje.append(t.Aplikacje(street,house,city,zrodlo,registration_date,fk_klienci))

for i in range(LICZBA_KART):
    number = random.randint(1000000000000000,9999999999999999)
    security= random.randint(100,999)
    fk_klienci = random.choice([x.args[x.primary_key] for x in aplikacje])
    karty.append(t.Karty(number,security,fk_klienci))

for i in range(LICZBA_WYKORZYSTAN):
    nr = random.choice([samochod.args[samochod.primary_key] for samochod in samochody])
    pesel = random.choice([x.args[x.primary_key] for x in kierowcy])
    data_rozpoczecia=t.get_random_date(date(2016,6,30))
    data_zakonczenia=t.get_random_date(data_rozpoczecia)
    wykorzystania.append(t.Wykorzystania(nr,pesel,data_rozpoczecia,data_zakonczenia))

for i in range(LICZBA_PRZEJAZDOW):
    wykorzystanie = random.choice(wykorzystania)
    date = t.get_random_date(wykorzystanie.args[2][1],wykorzystanie.args[3][1])
    ocena = random.randint(1,5)
    poczatek_ulica=random.choice(streets)
    poczatek_nrdomu=random.randint(1,200)
    poczatek_miasto=random.choice(cities)
    koniec_ulica =random.choice(streets)
    koniec_nrdomu=random.randint(1, 200)
    koniec_miasto=random.choice(cities)
    koszt = random.randint(15,50)
    napiwek = random.randint(0,20)
    czas = random.randint(1,3600)
    fk_klienci = random.choice(klienci)
    fk_kierowcy = wykorzystanie.args[1][1]
    fk_dyspozytorzy = random.choice(dyspozytorzy)
    przejazdy.append(t.Przejazdy(date,i,ocena,poczatek_ulica,poczatek_nrdomu,poczatek_miasto,koniec_ulica,koniec_nrdomu,koniec_miasto,koszt,napiwek,czas,fk_klienci,fk_kierowcy,fk_dyspozytorzy))


