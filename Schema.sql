-- Tworzenie Tabel
CREATE TABLE Produkty (
	produkt_id INT PRIMARY KEY,
    producent_id INT,
    model_id INT,
    kategorie_id INT,
    wymiar_id INT,
    opis VARCHAR(50),
    ilosc INT DEFAULT 0,
    cena DOUBLE NOT NULL
);


CREATE TABLE Producenci (
	producent_id INT PRIMARY KEY,
    producent VARCHAR(30),
    dane_kontaktowe_id INT
);


ALTER TABLE Produkty
ADD FOREIGN KEY(producent_id)
REFERENCES Producenci(producent_id)
ON DELETE SET NULL;

CREATE TABLE Dane_kontaktowe(
	dane_kontaktowe_id INT PRIMARY KEY,
    adres_email VARCHAR(20),
    numer_telefonu VARCHAR(15),
    adres VARCHAR(30)
);

ALTER TABLE Producenci
ADD FOREIGN KEY(dane_kontaktowe_id)
REFERENCES Dane_kontaktowe(dane_kontaktowe_id)
ON DELETE SET NULL;

CREATE TABLE Zamowienie(
	zamowienie_id INT PRIMARY KEY,
    produkt_id INT,
    kasa_id INT,
    FOREIGN KEY(produkt_id) REFERENCES Produkty(produkt_id) ON DELETE SET NULL
);


CREATE TABLE Modele(
	model_id INT PRIMARY KEY,
    producent_id INT,
    model VARCHAR(50),
    rok_produkcji INT,
    FOREIGN KEY(producent_id) REFERENCES Producenci(producent_id) ON DELETE SET NULL
);

ALTER TABLE Produkty
ADD FOREIGN KEY(model_id)
REFERENCES Modele(model_id)
ON DELETE SET NULL;


CREATE TABLE Kategorie(
	kategorie_id INT PRIMARY KEY,
    kategoria VARCHAR(30)
);

ALTER TABLE Produkty
ADD FOREIGN KEY(kategorie_id)
REFERENCES Kategorie(kategorie_id)
ON DELETE SET NULL;

-- skala w mm
CREATE TABLE Wymiary(
	wymiar_id INT PRIMARY KEY,
    wysokosc INT NOT NULL,
    szerokosc INT NOT NULL,
    glebokosc INT NOT NULL
);

ALTER TABLE Produkty
ADD FOREIGN KEY(wymiar_id)
REFERENCES Wymiary(wymiar_id)
ON DELETE SET NULL;

CREATE TABLE Uprawnienia(
	uprawnienie_id INT PRIMARY KEY,
    uprawnienie VARCHAR(30)
);

-- haslo przechowywane w formie hashy (planowane 256 bitow)
CREATE TABLE Dane_logowania(
	dane_logowania_id INT PRIMARY KEY,
    login VARCHAR(20),
    haslo VARCHAR(64)
);

CREATE TABLE Pracownik(
	pracownik_id INT PRIMARY KEY,
    dane_logowania_id INT,
    dane_kontaktowe_id INT,
    uprawnienie_id INT,
    imie VARCHAR(20),
    nazwisko VARCHAR(20),
    FOREIGN KEY(dane_logowania_id) REFERENCES Dane_logowania(dane_logowania_id) ON DELETE SET NULL,
    FOREIGN KEY(dane_kontaktowe_id) REFERENCES Dane_kontaktowe(dane_kontaktowe_id) ON DELETE SET NULL,
    FOREIGN KEY(uprawnienie_id) REFERENCES Uprawnienia(uprawnienie_id) ON DELETE SET NULL
);



DESCRIBE Pracownik;
