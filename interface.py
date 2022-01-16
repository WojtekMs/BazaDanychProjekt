#!/usr/bin/env python

import os
import argparse

import mysql.connector
from mysql.connector import FieldType

from sklep.select import searching, select_product_between_prices, select_product_by_price, Operand, options, show_products
from sklep.insert import adding_product
from sklep.update import edit_product
from sklep.utils import pretty_print
from sklep.delete import deleting_product

###############################################################################

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("db",
                        help="Nazwa twojej bazy danych (sklep_rtv, sklep)")
    args = parser.parse_args()

    host = 'localhost'
    port = 3306
    user = 'root'
    password = os.environ["MYSQL_PASS"]
    db = args.db

    conn = mysql.connector.connect(host=host,
                                   user=user,
                                   password=password,
                                   port=port,
                                   database=db,
                                   buffered=True,
                                   raw=False)

    cursor = conn.cursor()

    description, rows = select_product_by_price(cursor, 929, Operand.EQUAL)
    description2, rows2 = select_product_between_prices(cursor, 929, 1872)
    pretty_print(description, rows)
    pretty_print(description2, rows2)

###############################################################################

    #testowanie wyszukiwania produktu

    #category = input("Podaj kategorie: ")
    #price_from = float(input("Podaj od jakiej kwoty wyszukiwac: "))
    #price_to = float(input("Podaj do jakiej kwoty wyszukiwac: "))
    #producer = input("Podaj producenta: ")

    #print("Wyszukane przez ciebie produkty: ")

    #description, rows = searching(cursor, category, price_from, price_to, producer)
    #pretty_print(description, rows)
    #conn.close()

###############################################################################

    # testowanie dodawania produktu
    #producer = input("Producent: ")
    #model = input("Model urzadzenia: ")
    #year_of_production = int(input("Rok produkcji: "))
    #print("Podaj wymiary urzadzenia: ")
    #height = int(input("Wysokosc: "))
    #width = int(input("Szerokosc: "))
    #depth = int(input("Glebokosc: "))
    #category = input("Kategoria: ")
    #name = input("Opis: ")
    #quantity = int(input("Ilosc: "))
    #price = float(input("Cena: "))

    #print("Dodany przez ciebie produkt: ")

    #adding_product(cursor, producer, model, year_of_production, height, width, depth,category, name, quantity, price)

###############################################################################

    #testowanie edytowania produktu (ilosc)
    #model = input("Podaj model produktu, ktory chcesz edytowac: ")
    #new_quantity = int(input("Podaj nowa ilosc: "))

    #edit_product(cursor, new_quantity, model)

    #description, rows = show_products(cursor)
    #pretty_print(description, rows)

###############################################################################

    # testowanie usuwania produktu po modelu
    #model = input("Podaj model urzadzenia, ktore chcesz usunac: ")

    #deleting_product(cursor, model)

###############################################################################

    conn.commit() # sprawia ze zapisywane sa zmiany w bazie
    conn.close()

if __name__ == "__main__":
    main()
