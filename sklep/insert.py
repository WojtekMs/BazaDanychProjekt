# tutaj scenariusz uzycia:
# - dodawanie produktu
# - zamowienie produktu
from sklep.utils import convert_types, pretty_print

from enum import Enum, auto

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