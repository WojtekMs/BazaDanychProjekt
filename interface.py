#!/usr/bin/env python

import MySQLdb
import os
import argparse


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

    # Example of how to insert new values:
    conn.query("INSERT INTO Uprawnienia (uprawnienie_id, uprawnienie) VALUES(31, 'admin')")
    conn.commit()

    # Example of how to fetch table data:
    conn.query("SELECT * FROM Uprawnienia")
    result = conn.store_result()
    for i in range(result.num_rows()):
        print(result.fetch_row())

if __name__ == "__main__":
    main()
