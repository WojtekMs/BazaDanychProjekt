#!/usr/bin/env python

import argparse

import mysql.connector

from sklep.ConsoleView import ConsoleView, ACTION
from sklep.select import searching, select_contact_data, select_employees, select_login_data, select_product_between_prices, select_product_by_price, Operand, options, select_product_get_input, show_products, show_workers, select_authentication, select_product_get_query
from sklep.insert import add_product_get_input, add_product, add_account_get_input, add_account, add_order_get_input, add_order
from sklep.update import ed_product_get_input, ed_product, edit_account_by_admin, edit_account_get_input, edit_account
from sklep.utils import choose_one_of, execute_query, get_headers, get_safe_str_input, pretty_print, login, get_auth, connect
from sklep.delete import del_product_get_input, del_product, del_employee_get_input, del_employee

###############################################################################


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("db",
                        help="Nazwa twojej bazy danych (sklep_rtv, sklep)")
    args = parser.parse_args()

    choice = choose_one_of(["1. Logowanie", "2. Dostep klienta"])
    if choice == "1. Logowanie":
        user, password = login()
    else:
        user, password = "klient", ""

    conn = connect(user=user, password=password, db=args.db)
    cursor = conn.cursor()
    
    auth = get_auth(cursor, user)
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
            desk_nr = add_order(cursor, args)
            print(f"Produkt zamówiony w kasie nr {desk_nr}!")
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
        elif action == ACTION.SELECT_EMPLOYEE:
            description, rows = select_employees(cursor)
            pretty_print(description, rows)
        elif action == ACTION.SELECT_CONTACT_DATA:
            description, rows = select_contact_data(cursor)
            pretty_print(description, rows)
        elif action == ACTION.SELECT_LOGIN_DATA:
            description, rows = select_login_data(cursor)
            pretty_print(description, rows)
        elif action == ACTION.SELECT_AUTH:
            description, rows = select_authentication(cursor)
            pretty_print(description, rows)
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
# - usuwanie konta powinno robic DELETE USER
# - aktualnie nie wiadomo czemu, trzeba dodac na koncu \r zeby poprawnie wyszukac kategorie!

# NOTATKI 24.01.2022
# - zrobic wyswietlanie wszystkich pracownikow
if __name__ == "__main__":
    main()
