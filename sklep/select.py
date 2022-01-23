from sklep.utils import choose_one_of, convert_types, pretty_print, get_safe_str_input, get_typed_input

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
        SELECT opis, ilosc, cena
FROM Produkty
INNER JOIN Kategorie ON Produkty.kategorie_id=Kategorie.kategorie_id
INNER JOIN Producenci ON Produkty.producent_id=Producenci.producent_id
WHERE Kategorie.kategoria = '%s'
AND cena > %s AND cena < %s
AND Producenci.producent = '%s';
""" % (category, price_from, price_to, producer))

    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows

def select_product_get_input():
    producer = get_safe_str_input("Producent []: ")
    model = get_safe_str_input("Model []: ")
    category = get_safe_str_input("Kategoria []: ")
    search_by_price = get_safe_str_input("Wyszukuj po cenie [N/t]: ").lower() == "t"
    equal_price, min_price, max_price = None, None, None
    if search_by_price:
        actions = ["1. Rowna cena", "2. Cena mniejsza niż", "3. Cena większa niż", "4. Cena pomiędzy dwoma wartościami"]
        choice = choose_one_of(actions)
        if choice == actions[0]:
            equal_price = get_typed_input("Podaj cenę: ", float)
        elif choice == actions[1]:
            max_price = get_typed_input("Podaj maksymalną cenę: ", float)
        elif choice == actions[2]:
            min_price = get_typed_input("Podaj minimalną cenę: ", float)
        elif choice == actions[3]:
            min_price = get_typed_input("Podaj mniejszą cenę: ", float)
            max_price = get_typed_input("Podaj większą cenę: ", float)
    return producer, model, category, equal_price, min_price, max_price

def select_product_get_query(args):
    queries = []
    query = f"SELECT Produkty.* FROM Produkty "
    if args[0] != "":
        query += "INNER JOIN Producenci ON Produkty.producent_id=Producenci.producent_id "
        queries.append(f"Producenci.producent='{args[0]}' ")
    if args[1] != "":
        query += "INNER JOIN Modele ON Produkty.model_id=Modele.model_id "
        queries.append(f"Modele.model='{args[1]}' ")
    if args[2] != "":
        query += "INNER JOIN Kategorie ON Produkty.kategorie_id=Kategorie.kategorie_id "
        queries.append(f"Kategorie.kategoria='{args[2]}' ")
    if args[3]:
        queries.append(f"Produkty.cena={args[3]} ")
    elif args[4] and args[5]:
        queries.append(f"Produkty.cena BETWEEN {args[4]} AND {args[5]} ")
    elif args[4]:
        queries.append(f"Produkty.cena > {args[4]} ")
    elif args[5]:
        queries.append(f"Produkty.cena < {args[5]} ")
    
    for id, q in enumerate(queries):
        if id == 0:
            query += "WHERE "
        else:
            query += "AND "
        query += q
    query += ";"
    return query

def show_products(cursor):
    cursor.execute("""SELECT * FROM kategorie;""")
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows

def show_workers(cursor):
    cursor.execute("""SELECT imie, nazwisko FROM pracownik;""")
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


def select_orders(cursor):
    cursor.execute("SELECT * FROM zamowienie")
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows

def select_employees(cursor):
    cursor.execute("SELECT * FROM pracownik")
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows

def select_contact_data(cursor):
    cursor.execute("SELECT * FROM dane_kontaktowe")
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows

def select_login_data(cursor):
    cursor.execute("SELECT * FROM dane_logowania")
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows

def select_authentication(cursor):
    cursor.execute("SELECT * FROM uprawnienia")
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows
