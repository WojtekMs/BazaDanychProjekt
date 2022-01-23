#!/usr/bin/env python

import argparse

import mysql.connector

from sklep.ConsoleView import ConsoleView, ACTION
from sklep.select import searching, select_contact_data, select_employees, select_login_data, select_product_between_prices, select_product_by_price, Operand, options, select_product_get_input, show_products, show_workers, select_authentication, select_product_get_query
from sklep.insert import add_product_get_input, add_product, add_account_get_input, add_account, add_order_get_input, add_order
from sklep.update import ed_product_get_input, ed_product, edit_account_by_admin, edit_account_get_input, edit_account
from sklep.utils import execute_query, get_headers, get_safe_str_input, pretty_print, login, get_auth
from sklep.delete import del_product_get_input, del_product, del_employee_get_input, del_employee

###############################################################################


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("db",
                        help="Nazwa twojej bazy danych (sklep_rtv, sklep)")
    args = parser.parse_args()


    user, password = login()

    host = 'localhost'
    port = 3306
    user = user
    password = password
    db = args.db

    conn = mysql.connector.connect(host=host,
                                user=user,
                                password=password,
                                port=port,
                                database=db,
                                buffered=True,
                                raw=False)

    cursor = conn.cursor()
    

    auth = get_auth(user)
    view = ConsoleView(auth)
    view.display_menu()
    action = view.choose_action()
    while action != ACTION.QUIT:
        if action == ACTION.SELECT_PRODUCT:
            args = select_product_get_input()
            query = select_product_get_query(args)
            description, rows = execute_query(cursor, query)
            pretty_print(description, rows)
        elif action == ACTION.ADD_PRODUCT:
            args = add_product_get_input()
            add_product(cursor, args)
            print("Produkt dodany!")
        elif action == ACTION.ADD_ORDER:
            args = add_order_get_input()
            add_order(cursor, args)
            print("Produkt zamówiony!")
        elif action == ACTION.ADD_ACCOUNT:
            args = add_account_get_input()
            add_account(cursor, args)
            print("Konto zostalo dodane!")
        elif action == ACTION.EDIT_PRODUCT:
            args = ed_product_get_input()
            ed_product(cursor, args)
            print("Produkt zostal zedytowany!")
        elif action == ACTION.EDIT_ACCOUNT:
            args = edit_account_get_input()
            edit_account(cursor, args)
            print("Konto zostało zedytowane")
        elif action == ACTION.DELETE_PRODUCT:
            args = del_product_get_input()
            del_product(cursor, args)
            print("Produkt usuniety!")
        elif action == ACTION.DELETE_EMPLOYEE:
            args = del_employee_get_input()
            del_employee(cursor, args)
            print("Konto zostalo usuniete!")

        view.display_menu()
        action = view.choose_action()

    conn.commit()  # sprawia ze zapisywane sa zmiany w bazie
    conn.close()

    print("Do zobaczenia!")


# NOTATKI 22.01.2022
# bardzo wazne, zeby zwracac uwage na typ danych, ktore sa wprowadzane, za pomoca parametru do funkcji get_typed_input [w pliku sklep.utils]
# gdy input jest typu str, nalezy go poprawnie zwalidowac aby uniknac SQL injection za pomoca funkcji get_safe_str_input [w pliku sklep.utils]
# w zaleznosci od uzytkownika rozne akcje sa mozliwe do wykonania

# NOTATKI 23.01.2022
# - co w sytuacji gdy chce edytowac produkt, ktorego nie ma w bazie danych? [aktualnie wyswietla tylko OK]
# - czy powinnismy dbac o to, zeby e-mail i uprawnienia byly poprawne?
# - czy numer telefonu powinien byc int?
# - należy dodać ROLE odpowiadajace: klientowi, pracownikowi, adminowi
# - dodawanie konta powinno robic CREATE USER WITH ROLE
# - usuwanie konta powinno robic DELETE USER
# - aktualnie nie wiadomo czemu, trzeba dodac na koncu \r zeby poprawnie wyszukac kategorie!
if __name__ == "__main__":
    main()
