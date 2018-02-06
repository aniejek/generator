DROP TABLE Przejazdy;
DROP TABLE Kierowcy;
DROP TABLE Dyspozytorzy;
DROP TABLE Klienci;
DROP TABLE Samochody;
DROP TABLE Smieci;
DROP TABLE Adres;
DROP TABLE Godzina;
DROP TABLE Data;

CREATE TABLE Data (
	id int not null auto_increment,
	Rok varchar(4) not null,
	Miesiac varchar(2) not null,
	Dzien varchar(2) not null,
	Swieto char(3) not null,
	primary key (id)
);

CREATE TABLE Godzina (
	id int not auto_increment,
	Godzina varchar(2) not null,
	Minuta varchar(2) not null,
	primary key (id)
);

CREATE TABLE Adres (
	id int not null auto_increment,
	Miasto varchar(20) not null,
	Ulica varchar(15) not null,
	Nr_domu varchar(300) not null,
	primary key(id)
);

CREATE TABLE Smieci (
	id int not null auto_increment,
	Ocena varchar(15) not null,
	primary key(id)
);

CREATE TABLE Samochody (
	id int not null auto_increment,
	Model varchar(15) not null,
	Marka varchar(15) not null,
	Rocznik char(4) not null,
	primary key(id)
);

CREATE TABLE Dyspozytorzy (
	id int not null auto_increment,
	Imie_i_nazwisko varchar(50) not null,
	Miasto varchar(20) not null,
	primary key(id)
);

CREATE TABLE Kierowcy (
	id int not null auto_increment,
	Imie_i_nazwisko varchar(50) not null,
	Polecajacy int,
	Staz varchar(7) not null,
	Aktualnosc bit not null,
	primary key(id),
	foreign key(Polecajacy) references Kierowcy(id)
);

CREATE TABLE Klienci (
	id int not null auto_increment,
	Imie_i_nazwisko varchar(50) not null,
	Adres int not null,
	Czy_korzysta_z_aplikacji bit not null,
	Data_instalacji_aplikacji int,
	Skad_sie_dowiedzial varchar(35),
	foreign key(Adres) references Adres(id),
	foreign key(Data_instalacji_aplikacji) references Data(id),
	primary key(id)
);

CREATE TABLE Przejazdy (
	Napiwek money,
	Koszt money not null,
	Ocena int,
	Nr_faktury int,
	Czas int not null,
	FK_Dyspozytorzy int,
	FK_Klienci int,
	FK_Kierowcy int,
	FK_Poczatki int,
	FK_Samochody int,
	FK_Konce int,
	FK_Data int,
	FK_Godzina int,
	FK_Smieci int,
	Foreign key(FK_Dyspozytorzy) references Dyspozytorzy(id),
	Foreign key(FK_Klienci) references Klienci(id),
	Foreign key(FK_Kierowcy) references Kierowcy(id),
	Foreign key(FK_Poczatki) references Adres(id),
	Foreign key(FK_Samochody) references Samochody(id),
	Foreign key(FK_Konce) references Adres(id),
	Foreign key(FK_Data) references Data(id),
	Foreign key(FK_Godzina) references Godzina(id),
	Foreign key(FK_Smieci) references Smieci(id),
	Constraint id primary key (FK_Dyspozytorzy,
		FK_Klienci, FK_Kierowcy, FK_Poczatki, FK_Samochody,
		FK_Konce, FK_Data, FK_Godzina, FK_Smieci)
);
