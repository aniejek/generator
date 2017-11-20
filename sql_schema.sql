CREATE TABLE Dyspozytornie (
	Miasto varchar(20) NOT NULL,
	PRIMARY KEY (Miasto)
);

CREATE TABLE Dyspozytorzy ( 
	FK_Dyspozytornie varchar(20) NOT NULL,
	FOREIGN KEY(FK_Dyspozytornie),
	Imie varchar(20) NOT NULL,
	Nazwisko varchar(20) NOT NULL,
	PESEL char(11) NOT NULL,
	PRIMARY KEY(PESEL)
);

CREATE TABLE Kierowcy (
	PESEL char(11) NOT NULL,
	Imie varchar(20) NOT NULL,
	Nazwisko varchar(20) NOT NULL,
	Data_rejestracji datetime NOT NULL,
	PRIMARY KEY(PESEL)
);

CREATE TABLE Klienci (
	ID int NOT NULL,
	Imie varchar(20) NOT NULL,
	Nazwisko varchar(20) NOT NULL,
	Telefon varchar(11) NOT NULL,
	PRIMARY KEY(ID)
);

CREATE TABLE Aplikacje (
	Ulica varchar(30),
	Miejscowosc varchar(30) NOT NULL,
	Zrodlo_wiedzy varchar(60) NOT NULL,
	Data_rejestracji datetime NOT NULL,
	Numer_domu int NOT NULL,
	FK_Klienci int NOT NULL,
	FOREIGN KEY(FK_Klienci),
	PRIMARY KEY(FK_Klienci)
);

CREATE TABLE Karty (
	Numer varchar(24) NOT NULL,
	Kod char(3) NOT NULL,
	FK_Klienci int NOT NULL,
	FOREIGN KEY(FK_Klienci),
	PRIMARY KEY(Numer)
);

CREATE TABLE Przejazdy (
	ID int NOT NULL,
	Data datetime NOT NULL,
	Godzina time NOT NULL,
	Ocena int,
	Poczatek_ulica varchar(30),
	Poczatek_miejscowosc varchar(30) NOT NULL,
	Poczatek_numer_domu int NOT NULL,
	Koniec_ulica varchar(30),
	Koniec_miejscowosc varchar(30) NOT NULL,
	Koniec_numer_domu int NOT NULL,
	Koszt smallmoney NOT NULL,
	Napiwek smallmoney,
	Czas time NOT NULL,
	FK_Klienci int NOT NULL,
	FK_Kierowcy char(11) NOT NULL,
	FK_Dyspozytorzy char(11) NOT NULL,
	FOREIGN KEY(FK_Klienci),
	FOREIGN KEY(FK_Kierowcy),
	FOREIGN KEY(FK_Dyspozytorzy),
	PRIMARY KEY(ID)
);
	