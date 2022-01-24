# tutaj scenariusz uzycia:
# - dodawanie produktu
# - zamowienie produktu
from sklep.utils import convert_types, pretty_print, get_typed_input, get_safe_str_input, login

from enum import Enum, auto
import random
import hashlib

###############################################################################


def adding_product(cursor, producer, model, year_of_production, height, width,
                   depth, category, name, quantity, price):
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


def add_product(cursor, args):
    adding_product(cursor, args[0], args[1], args[2], args[3], args[4],
                   args[5], args[6], args[7], args[8], args[9])


def add_product_get_input():
    print("Dodaj produkt\n")
    producer = get_safe_str_input("Producent: ")
    model = get_safe_str_input("Model urzadzenia: ")
    year_of_production = get_typed_input("Rok produkcji: ", int)
    print("Podaj wymiary urzadzenia: ")
    height = get_typed_input("Wysokosc: ", int)
    width = get_typed_input("Szerokosc: ", int)
    depth = get_typed_input("Glebokosc: ", int)
    category = get_safe_str_input("Kategoria: ")
    name = get_safe_str_input("Opis: ")
    quantity = get_typed_input("Ilosc: ", int)
    price = get_typed_input("Cena: ", float)
    print()
    return (producer, model, year_of_production, height, width, depth,
            category, name, quantity, price)


###############################################################################


def add_order(cursor, product_id):
    cash_desk_nr = random.randint(1, 10)
    cursor.execute(
        f"INSERT INTO zamowienie (produkt_id, kasa_id) VALUES({product_id}, {cash_desk_nr});"
    )
    return cash_desk_nr


def add_ord(cursor, arg):
    add_order(cursor, arg)


def add_order_get_input():
    product_id = get_typed_input(
        "Podaj numer ID produktu, który chcesz zamówić: ", int)
    return (product_id)


###############################################################################


# Dodawanie konta przez admina
def add_account_by_admin(cursor, login, password, email, phnumber, address,
                         auth, first_name, last_name):
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

    cursor.execute(
        f"CREATE USER IF NOT EXISTS '{login}'@'localhost' IDENTIFIED BY '{password}' DEFAULT ROLE '{auth}';"
    )


def add_account(cursor, args):
    add_account_by_admin(cursor, args[0], args[1], args[2], args[3], args[4],
                         args[5], args[6], args[7])


def add_account_get_input():
    print("Dodaj Konto\n")
    print("Wprowadz Dane: \n")
    user, password = login()
    email = get_safe_str_input("Email: ")
    phnumber = get_safe_str_input("Numer telefonu: ")
    address = get_safe_str_input("Adres: ")
    auth = get_safe_str_input("Uprawnienia: ")
    first_name = get_safe_str_input("Imie: ")
    last_name = get_safe_str_input("Nazwisko: ")
    print()
    return (user, password, email, phnumber, address, auth, first_name,
            last_name)
