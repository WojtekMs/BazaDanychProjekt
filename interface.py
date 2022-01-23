#!/usr/bin/env python

import argparse

import mysql.connector

from sklep.ConsoleView import ConsoleView, ACTION
from sklep.select import searching, select_contact_data, select_employees, select_login_data, select_product_between_prices, select_product_by_price, Operand, options, show_products, show_workers, select_authentication
from sklep.insert import add_product_get_input, add_product, add_account_get_input, add_account, add_order_get_input, add_order
from sklep.update import ed_product_get_input, ed_product, edit_account_by_admin, edit_account_get_input, edit_account
from sklep.utils import get_headers, get_safe_str_input, pretty_print, login, get_auth
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
    if action == ACTION.SELECT_PRODUCT:
        pass
        # gather input
        # perform query
        # display result
    elif action == ACTION.ADD_PRODUCT:
        args = add_product_get_input()
        add_product(cursor, args)
        print("Produkt dodany!")
    elif action == ACTION.ADD_ORDER:
        args = add_order_get_input()
        add_order(cursor, args)
        print("Produnkt zamówiony!")
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

    # testowanie dodawania pracownika
    #login = input("Podaj login: ")
    #password = input("Podaj haslo: ")
    #email = input("Podaj e-mail: ")
    #phnumber = input("Podaj numer telefonu: ")
    #address = input("Podaj adres: ")
    #auth = input("Podaj uprawnienie: ")
    #first_name = input("Podaj imie: ")
    #last_name = input("Podaj nazwisko: ")

    #add_account_by_admin(cursor, login, password, email, phnumber, address, auth, first_name, last_name)

    #description, rows = show_workers(cursor)
    #pretty_print(description, rows)

    ##############################################################################

    # testowanie edycji danych pracownika
    # worker_id = int(input("Podaj id pracownika, ktorego chcesz edytowac: "))
    # newLogin = input("Podaj nowy login: ")
    # newPassword = input("Podaj nowe haslo: ")
    # newAdressEmail = input("Podaj nowy e-mail: ")
    # newPhnumber = input("Podaj nowy numer telefonu: ")
    # newAddress = input("Podaj nowy adres: ")
    # newName = input("Podaje nowe imie: ")
    # newSurname = input("Podaj nowe nazwisko: ")

    # edit_account_by_admin(cursor, newLogin, newPassword, worker_id, newAdressEmail, newPhnumber,
    #                       newAddress, newName, newSurname)

    # description, rows = show_workers(cursor)
    # pretty_print(description, rows)

    conn.commit()  # sprawia ze zapisywane sa zmiany w bazie
    conn.close()


# NOTATKI 22.01.2022
# bardzo wazne, zeby zwracac uwage na typ danych, ktore sa wprowadzane, za pomoca parametru do funkcji get_typed_input [w pliku sklep.utils]
# gdy input jest typu str, nalezy go poprawnie zwalidowac aby uniknac SQL injection za pomoca funkcji get_safe_str_input [w pliku sklep.utils]
# w zaleznosci od uzytkownika rozne akcje sa mozliwe do wykonania
# TODO:
# - podczas edytowania pracownika lepiej podac uprawnienie po nazwie, a nie po id
# - dodac kod do pozostalych akcji oprocz ACTION.SELECT_PRODUCT wzorujac sie na ACTION.ADD_PRODUCT

# NOTATKI 23.01.2022
# - co w sytuacji gdy chce edytowac produkt, ktorego nie ma w bazie danych? [aktualnie wyswietla tylko OK]
# - czy powinnismy dbac o to, zeby e-mail i uprawnienia byly poprawne?
# - należy dodać ROLE odpowiadajace: klientowi, pracownikowi, adminowi
# - dodawanie konta powinno robic CREATE USER WITH ROLE
# - usuwanie konta powinno robic DELETE USER
if __name__ == "__main__":
    main()
