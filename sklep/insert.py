# tutaj scenariusz uzycia:
# - dodawanie produktu
# - zamowienie produktu
from sklep.utils import convert_types, pretty_print

from enum import Enum, auto
import random
import hashlib

def adding_product(cursor, producer, model, year_of_production, height, width, depth,
                                       category, name, quantity, price):
    #dodanie do tabeli Modele
    cursor.execute("""
        INSERT INTO modele (producent_id, model, rok_produkcji)
        VALUES ((select producent_id from producenci where producent = '%s'), '%s', %s);
""" % (producer, model, year_of_production))

    #dodanie do tabeli Wymiary
    cursor.execute("""
    INSERT INTO wymiary (wysokosc, szerokosc, glebokosc)
    VALUES (%s, %s, %s);
""" % (height, width, depth))

    #dodanie do tabeli Produkty
    cursor.execute("""
        INSERT INTO produkty (producent_id, model_id, kategorie_id, wymiar_id, opis, ilosc, cena)
    VALUES (
    (select producent_id from producenci where producent = '%s'),
    (select model_id from modele where model = '%s'),
    (select kategorie_id from kategorie where kategoria = '%s'),
    (select wymiar_id FROM wymiary order by wymiar_id DESC LIMIT 1),
'%s', %s, %s);
""" % (producer, model, category, name, quantity, price))

    #wyswietlenie dodanego produktu
    #cursor.execute("""SELECT opis, ilosc, cena FROM produkty ORDER BY produkt_id DESC LIMIT 1""")

    #rows = cursor.fetchall()
    #rows = convert_types(rows)
    #return cursor.description, rows

def add_order(cursor, product_id):
    
    cursor.execute(f"INSERT INTO zamowienie (produkt_id, kasa_id) VALUES({product_id}, {random.randint(1, 10)});")

# Dodawanie konta przez admina
def add_account_by_admin(cursor, login, password, email, phnumber, address, auth, first_name, last_name):
    cursor.execute("""
    INSERT INTO dane_logowania (login, haslo) VALUES ('%s', SHA2('%s', 256));
    """ % (login, password))

    cursor.execute("""
    INSERT INTO dane_kontaktowe (adres_email, numer_telefonu, adres) 
        VALUES ('%s', '%s', '%s');
    """ % (email, phnumber, address))

    cursor.execute("""
    INSERT INTO pracownik(dane_logowania_id, dane_kontaktowe_id, uprawnienie_id, imie, nazwisko)
    VALUES(
        (SELECT dane_logowania_id FROM dane_logowania WHERE login = '%s'),
        (SELECT dane_kontaktowe_id FROM dane_kontaktowe WHERE adres_email = '%s'),
        (SELECT uprawnienie_id FROM uprawnienia WHERE uprawnienie = '%s'),
        '%s', '%s');
    """ % (login, email, auth, first_name, last_name))
