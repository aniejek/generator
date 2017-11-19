from random import randint
class Entity():
    def __init__(self):
        self.name = ""
        self.args = None
        self.primary_key = 0

    def to_sql(self, file):
        val_list = []
        col_list = []
        for arg in self.args:
            val_list.append(arg[1])
            col_list.append(arg[0])
        insert = 'INSERT INTO ' + self.name + ' ('
        for col in col_list:
            insert = insert + col + ', '
        insert[insert.len() - 2] = ')'
        values = 'values ('
        for val in val_list:
            try:
                int(val)
                values = values + str(val) + ', '
            except ValueError:
                values = values + "'" + val + "', "

        with open(file, 'a') as sql:
            insert.join(sql)
            values.join(sql)

    def to_csv(self, file):
        val_list = []
        for arg in self.args:
            val_list.append(arg[1])
        separator = ','
        line = separator.join(val_list)
        with open(file, 'a') as csv:
            line.join(csv)


def size_of_list(file):
    with open(file, 'r', encoding='utf8') as file:
        for i, line in enumerate(file):
            pass
        return i + 1


def take_random_line(file, size):
    with open(file, 'r+', encoding='utf8') as fnames:
        index = randint(0, size - 1)
        for i, line in enumerate(fnames):
            if i == index:
                return line[:-1]


class Dyspozytornie(Entity):
    def __init__(self, miasto):
        self.name = 'Dyspozytornie'
        self.args = [('Miasto', miasto)]
        self.primary_key = 0


class Dyspozytorzy(Entity):
    def __init__(self, imie, nazwisko, pesel, fk_dyspozytornie):
        self.name = 'Dyspozytorzy'
        self.args = [('Imie', imie), ('Nazwisko', nazwisko), ('PESEL', pesel),
                     ('FK_Dyspozytornie', fk_dyspozytornie)]
        self.primary_key = 2


class Kierowcy(Entity):
    def __init__(self, imie, nazwisko, pesel, data_rejestracji):
        self.name = 'Kierowcy'
        self.args = [('Imie', imie), ('Nazwisko', nazwisko), ('PESEL', pesel),
                     ('Data Rejestracji', data_rejestracji)]
        self.primary_key = 2


class Klienci(Entity):
    def __init__(self, imie, nazwisko, telefon, id):
        self.name = 'Klienci'
        self.args = [('Imie', imie), ('Nazwisko', nazwisko), ('Telefon', telefon),
                     ('Id', id)]
        self.primary_key = 0 #TODO


class Przejazdy(Entity):
    def __init__(self, data, id, ocena, poczatek_ulica, poczatek_numer_domu,
                 poczatek_miasto, koniec_ulica, koniec_numer_domu, koniec_miasto,
                 koszt, napiwek, czas, fk_klienci, fk_kierowcy, fk_dyspozytorzy):
        self.name = 'Przejazdy'
        self.args = [('Data', data), ('Id', id), ('Ocena', ocena),
                     ('Początek_ulica', poczatek_ulica),
                     ('Poczatek_numer_domu', poczatek_numer_domu),
                     ('Poczatek_miasto', poczatek_miasto),
                     ('Koniec_ulica', koniec_ulica),
                     ('Koniec_numer_domu', koniec_numer_domu),
                     ('Koniec_miasto', koniec_miasto), ('koszt', koszt),
                     ('Napiwek', napiwek), ('Czas', czas),
                     ('FK_Klienci', fk_klienci), ('FK_Kierowcy', fk_kierowcy),
                     ('FK_Dyspozytorzy', fk_dyspozytorzy)]
        self.primary_key = 1


class Aplikacje(Entity):
    def __init__(self, ulica, numer_domu, miasto, zrodlo, data_rejestracji,
                 fk_klienci):
        self.name = 'Aplikacje'
        self.args = [('Ulica', ulica), ('Numer_domu', numer_domu),
                     ('Miasto', miasto), ('Skad_sie_dowiedzial', zrodlo),
                     ('Data_rejestracji', data_rejestracji),
                     ('FK_Klienci', fk_klienci)]
        self.primary_key = 5


class Karty(Entity):
    def __init__(self, numer, kod, fk_klient):
        self.name = 'Karty'
        self.args = [('Numer', numer), ('Kod', kod), ('FK_Klient', fk_klient)]
        self.primary_key = 0


class Wykorzystania(Entity):
    def __init__(self, numer_rejestracja, pesel, data_rozpoczecia, data_zakonczenia):
        self.name = 'Wykorzystania'
        self.args = [('Numer_rejestracyjny', numer_rejestracja), ('PESEL', pesel),
                     ('Data_rozpoczecia', data_rozpoczecia), ('Data_zakonczenia', data_zakonczenia)]
        self.primary_key = 0#TODO


class Samochody(Entity):
    def __init__(self, numer_rejestracja, data_przegladu, marka, model, rocznik, czy_nasz):
        self.name = 'Samochody'
        self.args = [('Numer_rejestracyjny', numer_rejestracja), ('Data_ostatniego_przegladu',
                                                                  data_przegladu),
                     ('Marka', marka), ('Model', model), ('Rocznik', rocznik), ('Czyj', czy_nasz)]
        self.primary_key = 0

