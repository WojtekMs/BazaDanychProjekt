#!/usr/bin/env python

import MySQLdb
import os
import argparse


def options(conn):
    print("Wybierz opcje:\n 1. Wyszukiwanie\n 2. Dodawanie produktu\n 3. Usuwanie produktu")
    option = int(input("Podaj numer opcji: "))
    if option == 1:
        print("Wybrales opcje Wyszukiwanie")
        searching(conn)
    if option == 2:
        print("Wybrales opcje Dodawanie produktu")

def searching(conn):
    category = input("Podaj kategorie: ")
    price_from = int(input("Podaj od jakiej kwoty wyszukiwac: "))
    price_to = int(input("Podaj do jakiej kwoty wyszukiwac: "))
    producer = input("Podaj producenta: ")

    conn.query("""
        SELECT opis, ilosc, cena FROM produkty 
        WHERE kategorie_id IN (SELECT kategorie_id FROM kategorie WHERE kategoria = '%s')
        AND cena > %s AND cena < %s
        AND producent_id IN (SELECT producent_id FROM producenci WHERE producent = '%s');
""" % (category, price_from, price_to, producer))

    print("Wyszukane przez ciebie produkty: ")

    result = conn.store_result()
    for i in range(result.num_rows()):
        print(result.fetch_row())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("db", help="Nazwa twojej bazy danych (sklep_rtv, sklep)")
    args = parser.parse_args()

    host = 'localhost'
    port = 3306
    user = 'root'
    password = os.environ["MYSQL_PASS"]
    db = args.db

    conn = MySQLdb.Connection(
        host=host,
        user=user,
        passwd=password,
        port=port,
        db=db
    )

    options(conn)

    # Example of how to insert new values:
    #conn.query("INSERT INTO Uprawnienia (uprawnienie_id, uprawnienie) VALUES(31, 'admin')")
    #conn.commit()

    # Example of how to fetch table data:
    #conn.query("SELECT * FROM Uprawnienia")
    #result = conn.store_result()
    #for i in range(result.num_rows()):
    #    print(result.fetch_row())

if __name__ == "__main__":
    main()
