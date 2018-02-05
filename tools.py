# -*- coding: utf-8 -*-
from random import randint
from datetime import date

class Entity:
    def __init__(self):
        self.name = ""
        self.args = None
        self.primary_key = 0

    def to_sql(self, file):
        val_list = []
        col_list = []
        are_null = False
        for arg in self.args:
            if arg[1] == 'null':
                are_null = True
            val_list.append(str(arg[1]))
            col_list.append(arg[0])
        insert = 'INSERT INTO ' + self.name + ' ('
        columns = ', '.join(col_list)
        insert = insert + columns + ')'
        if are_null:
            values = ''
            for i, val in enumerate(val_list):
                if val == 'null':
                    values += val
                else:
                    values += "'" + val + "'"
                if i != len(val_list) - 1:
                    values += ','
        else:
            values = "'" + "', '".join(val_list) + "'"
        insert = insert + '\nVALUES (' + values + ');\n'
        with open(file, 'a', encoding='utf8') as sql:
            sql.write(insert)

    def to_csv(self, file):
        val_list = []
        for arg in self.args:
            val_list.append(str(arg[1]))
        separator = ','
        line = separator.join(val_list)
        with open(file, 'a', encoding='utf8') as csv:
            csv.write(line + '\n')

    def update(self, file, index, value):
        self.args[index] = (self.args[index][0], value)
        line = "UPDATE " + self.name + "\nSET " + str(self.args[0]) + " = "
        line += '"' + str(value) + '"\n' + 'WHERE ' + str(self.args[self.primary_key][0])
        line += ' = "' + str(self.args[self.primary_key][1]) + '";'
        with open(file, 'a', encoding='utf8') as sql:
            sql.write(line)


def clear_file(file, schema=""):
    with open(file, 'w') as file:
        file.write(schema + '\n')
        file.close()


def size_of_list(file):
    with open(file, 'r', encoding='utf8') as file:
    #with open(file, 'r') as file:
        for i, line in enumerate(file):
            pass
        return i + 1


def take_random_line(file, size):
    with open(file, 'r+', encoding='utf8') as fnames:
    #with open(file, 'r+') as fnames:
        index = randint(0, size - 1)
        for i, line in enumerate(fnames):
            if i == index:
                return line[:-1]


# Returns a random date higher than the given argument.
def get_random_date(begin=date(2016,6,30), end=date.today()):
    return date.fromordinal(randint(begin.toordinal(), end.toordinal()))

def generate_pesel(prev):
    new = ''
    inc_flag = True
    for c in prev[::-1]:
        if inc_flag:
            if c == '9':
                new = '0' + new
            else:
                new = str(int(c) + 1) + new
                inc_flag = False
        else:
            new = c + new
    return new


class Dyspozytornie(Entity):
    def __init__(self, miasto = ''):
        self.name = 'Dyspozytornie'
        self.args = [('Miasto', miasto)]
        self.primary_key = 0


class Dyspozytorzy(Entity):
    def __init__(self, imie = '', nazwisko = '', pesel = '', fk_dyspozytornie = ''):
        self.name = 'Dyspozytorzy'
        self.args = [('Imie', imie), ('Nazwisko', nazwisko), ('PESEL', pesel),
                     ('FK_Dyspozytornie', fk_dyspozytornie)]
        self.primary_key = 2


class Kierowcy(Entity):
    def __init__(self, imie = '', nazwisko = '', pesel = '', data_rejestracji = ''):
        self.name = 'Kierowcy'
        self.args = [('Imie', imie), ('Nazwisko', nazwisko), ('PESEL', pesel),
                     ('Data_Rejestracji', data_rejestracji)]
        self.primary_key = 2


class Klienci(Entity):
    def __init__(self, imie = '', nazwisko = '', telefon = '', id = ''):
        self.name = 'Klienci'
        self.args = [('Imie', imie), ('Nazwisko', nazwisko), ('Telefon', telefon),
                     ('Id', id)]
        self.primary_key = 3


class Przejazdy(Entity):
    def __init__(self, data = '', id = '', ocena = '', poczatek_ulica = '', poczatek_numer_domu = '',
                 poczatek_miasto = '', koniec_ulica = '', koniec_numer_domu = '', koniec_miasto = '',
                 koszt = '', napiwek = '', czas = '', godzina = '', nr_faktury = '', fk_klienci = '',
                 fk_kierowcy = '', fk_dyspozytorzy = '', fk_samochody = ''):
        self.name = 'Przejazdy'
        self.args = [('Data', data),
                     ('Id', id),
                     ('Ocena', ocena),
                     ('Poczatek_ulica', poczatek_ulica),
                     ('Poczatek_numer_domu', poczatek_numer_domu),
                     ('Poczatek_miasto', poczatek_miasto),
                     ('Koniec_ulica', koniec_ulica),
                     ('Koniec_numer_domu', koniec_numer_domu),
                     ('Koniec_miasto', koniec_miasto),
                     ('Koszt', koszt),
                     ('Napiwek', napiwek),
                     ('Czas', czas),
                     ('Godzina', godzina),
                     ('Nr_faktury', nr_faktury),
                     ('FK_Klienci', fk_klienci),
                     ('FK_Kierowcy', fk_kierowcy),
                     ('FK_Dyspozytorzy', fk_dyspozytorzy),
                     ('FK_Samochody',fk_samochody)]
        self.primary_key = 1


class Aplikacje(Entity):
    def __init__(self, ulica = '', numer_domu = '', miasto = '', zrodlo = '', data_rejestracji = '',
                 fk_klienci = ''):
        self.name = 'Aplikacje'
        self.args = [('Ulica', ulica), ('Numer_domu', numer_domu),
                     ('Miasto', miasto), ('Skad_sie_dowiedzial', zrodlo),
                     ('Data_rejestracji', data_rejestracji),
                     ('FK_Klienci', fk_klienci)]
        self.primary_key = 5


class Karty(Entity):
    def __init__(self, numer = '', kod = '', fk_klient = ''):
        self.name = 'Karty'
        self.args = [('Numer', numer), ('Kod', kod), ('FK_Klienci', fk_klient)]
        self.primary_key = 0


class Wykorzystania(Entity):
    def __init__(self, id, numer_rejestracja = '', pesel = '', data_rozpoczecia = '', data_zakonczenia = ''):
        self.name = 'Wykorzystania'
        self.args = [('ID', id), ('Numer_rejestracyjny', numer_rejestracja), ('PESEL', pesel),
                     ('Data_rozpoczecia', data_rozpoczecia), ('Data_zakonczenia', data_zakonczenia)]
        self.primary_key = 0


class Samochody(Entity):
    def __init__(self, numer_rejestracja = '', data_przegladu = '', marka = '', model = '', rocznik = '', czy_nasz = ''):
        self.name = 'Samochody'
        self.args = [('Numer_rejestracyjny', numer_rejestracja),
                     ('Data_ostatniego_przegladu', data_przegladu),
                     ('Marka', marka), ('Model', model), ('Rocznik', rocznik), ('Czyj', czy_nasz)]
        self.primary_key = 0

class Data(Entity):
    def __init__(self, data=''):
        self.args[('Data', data)]
        self.primary_key=0