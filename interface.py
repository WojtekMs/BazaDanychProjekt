#!/usr/bin/env python

import os
import argparse

import mysql.connector
from mysql.connector import FieldType

from sklep.select import searching, select_product_between_prices, select_product_by_price, Operand, options
from sklep.utils import pretty_print


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

    category = input("Podaj kategorie: ")
    price_from = int(input("Podaj od jakiej kwoty wyszukiwac: "))
    price_to = int(input("Podaj do jakiej kwoty wyszukiwac: "))
    producer = input("Podaj producenta: ")

    print("Wyszukane przez ciebie produkty: ")

    description, rows = searching(cursor, category, price_from, price_to, producer)
    pretty_print(description, rows)
    conn.close()


if __name__ == "__main__":
    main()
