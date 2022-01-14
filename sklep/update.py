# tutaj scenariusz uzycia:
# - edycja produktu

### TEST ###

from sklep.utils import convert_types, pretty_print

from enum import Enum, auto

def edit_product(cursor, producer, model, year_of_production, height, width, depth,
                                       category, name, quantity, price):
    # edycja produktu
    cursor.execute("""
        UPDATE Produkty SET ilosc = '%s' WHERE produkt_id='%s';
""" % (quantity, model))
    
    
# -- edytowanie produktu (po produkt_id; zmieniamy ilość)
# SELECT opis, ilosc, cena FROM Produkty WHERE produkt_id=2;
# UPDATE Produkty SET ilosc = 11 WHERE produkt_id=2;
# SELECT opis, ilosc, cena FROM Produkty WHERE produkt_id=2;


    #wyswietlenie dodanego produktu
    cursor.execute("""SELECT opis, ilosc, cena FROM produkty ORDER BY produkt_id DESC LIMIT 1""")

    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows
