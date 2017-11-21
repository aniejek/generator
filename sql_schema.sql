CREATE TABLE Dyspozytornie (
	Miasto varchar(20) NOT NULL,
	PRIMARY KEY (Miasto)
);

CREATE TABLE Dyspozytorzy ( 
	Imie varchar(20) NOT NULL,
	Nazwisko varchar(20) NOT NULL,
	PESEL char(11) NOT NULL,
	FK_Dyspozytornie varchar(20) NOT NULL,
	FOREIGN KEY(FK_Dyspozytornie),
	PRIMARY KEY(PESEL)
);

CREATE TABLE Kierowcy (
	Imie varchar(20) NOT NULL,
	Nazwisko varchar(20) NOT NULL,
	PESEL char(11) NOT NULL,
	Data_rejestracji datetime NOT NULL,
	PRIMARY KEY(PESEL)
);

CREATE TABLE Klienci (
	Imie varchar(20) NOT NULL,
	Nazwisko varchar(20) NOT NULL,
	Telefon varchar(11) NOT NULL,
	ID int NOT NULL,
	PRIMARY KEY(ID)
);

CREATE TABLE Aplikacje (
	Ulica varchar(30),
	Numer_domu int NOT NULL,
	Miasto varchar(30) NOT NULL,
	Skad_sie_dowiedzial varchar(60) NOT NULL,
	Data_rejestracji datetime NOT NULL,
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
	Data datetime NOT NULL,
	ID int NOT NULL,
	Ocena int,
	Poczatek_ulica varchar(30),
	Poczatek_numer_domu int NOT NULL,
	Poczatek_miasto varchar(30) NOT NULL,
	Koniec_ulica varchar(30),
	Koniec_numer_domu int NOT NULL,
	Koniec_miasto varchar(30) NOT NULL,
	Koszt smallmoney NOT NULL,
	Napiwek smallmoney,
	Czas time NOT NULL,
	FK_Klienci int NOT NULL,
	FK_Kierowcy char(11) NOT NULL,
	FK_Dyspozytorzy char(11) NOT NULL,
	Godzina time NOT NULL,
	FOREIGN KEY(FK_Klienci),
	FOREIGN KEY(FK_Kierowcy),
	FOREIGN KEY(FK_Dyspozytorzy),
	PRIMARY KEY(ID)
);
	
