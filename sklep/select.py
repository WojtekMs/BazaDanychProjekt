from sklep.utils import convert_types, pretty_print

from enum import Enum, auto


class Operand(Enum):
    LESS = auto()
    GREATER = auto()
    EQUAL = auto()


def select_product_by_price(cursor, price_threshold: float, operand: Operand):
    if operand == Operand.LESS:
        cursor.execute(
            f"SELECT * FROM Produkty WHERE cena < {price_threshold};")
    if operand == Operand.GREATER:
        cursor.execute(
            f"SELECT * FROM Produkty WHERE cena > {price_threshold};")
    if operand == Operand.EQUAL:
        cursor.execute(f"SELECT * FROM Produkty WHERE cena={price_threshold};")
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows


def select_product_between_prices(cursor, min_price: float, max_price: float):
    cursor.execute(
        f"SELECT * FROM Produkty WHERE cena > {min_price} AND cena < {max_price};"
    )
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows


def searching(cursor, category, price_from, price_to, producer):


    cursor.execute("""
        SELECT opis, ilosc, cena FROM produkty 
        WHERE kategorie_id IN (SELECT kategorie_id FROM kategorie WHERE kategoria = '%s')
        AND cena > %s AND cena < %s
        AND producent_id IN (SELECT producent_id FROM producenci WHERE producent = '%s');
""" % (category, price_from, price_to, producer))

    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows


def options(cursor):
    print(
        "Wybierz opcje:\n 1. Wyszukiwanie\n 2. Dodawanie produktu\n 3. Usuwanie produktu"
    )
    option = int(input("Podaj numer opcji: "))
    if option == 1:
        print("Wybrales opcje Wyszukiwanie")
        description, rows = searching(cursor)
        pretty_print(description, rows)
    if option == 2:
        print("Wybrales opcje Dodawanie produktu")
        description, rows = searching(cursor)
        pretty_print(description, rows)
