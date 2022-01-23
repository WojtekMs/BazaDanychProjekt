# tutaj scenariusz uzycia:
# - edycja produktu

from sklep.utils import convert_types, pretty_print, get_typed_input, get_safe_str_input

from enum import Enum, auto

###############################################################################

def edit_product(cursor, new_quantity, model):
    cursor.execute("""
        UPDATE Produkty
        INNER JOIN Modele ON Produkty.model_id=Modele.model_id
        SET Produkty.ilosc = %s
        WHERE Modele.model = '%s';
""" % (new_quantity, model))


def ed_product(cursor, args):
    edit_product(cursor, args[0], args[1])


def ed_product_get_input():
    print("Edytuj produkt\n")
    model = get_safe_str_input("Model urzadzenia: ")
    quantity = get_typed_input("Ilosc: ", int)
    print()
    return (model, quantity)

###############################################################################

# Edycja konta przez admina
def edit_account_by_admin(cursor, newLogin, newPassword, worker_id, newAdressEmail, newPhnumber,
                          newAddress, newName, newSurname):
    # Zmiana loginu i hasła
    cursor.execute("""
        UPDATE Dane_logowania
        INNER JOIN Pracownik ON Dane_logowania.dane_logowania_id=Pracownik.dane_logowania_id
        SET Dane_logowania.login = '%s',
        Dane_logowania.haslo = SHA2('%s', 256)
        WHERE Pracownik.pracownik_id = %s;
    """ % (newLogin, newPassword, worker_id))

    # Zmiana danych kontaktowych
    cursor.execute("""
        UPDATE Dane_kontaktowe
        INNER JOIN Pracownik ON Dane_kontaktowe.dane_kontaktowe_id=Pracownik.dane_kontaktowe_id
        SET Dane_kontaktowe.adres_email = '%s',
        Dane_kontaktowe.numer_telefonu = '%s',
        Dane_kontaktowe.adres = '%s'
        WHERE Pracownik.pracownik_id = %s;
    """ % (newAdressEmail, newPhnumber, newAddress, worker_id))

    # Zmiana imienia i nazwiska
    cursor.execute("""
        UPDATE Pracownik
        SET imie = '%s',
        nazwisko = '%s'
        WHERE pracownik_id = %s;
    """ % (newName, newSurname, worker_id))


def edit_account(cursor, args):
    edit_account_by_admin(cursor, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])

def edit_account_get_input():
    print("Edytuj konto\n")
    print("Wprowadz Dane: \n")
    worker_id = get_typed_input("Id pracownika", int)
    newLogin = get_safe_str_input("Nowy login: ")
    newPassword = get_safe_str_input("Nowe haslo: ")
    newAdressEmail = get_safe_str_input("Nowy adres email: ")
    newPhnumber = get_safe_str_input("Nowy numer telefonu: ")
    newAddress = get_typed_input("Nowy adres: ")
    newName = get_typed_input("Nowe imie: ")
    newSurname = get_typed_input("Nowe nazwisko: ")
    print()
    return (newLogin, newPassword, worker_id, newAdressEmail, newPhnumber,
            newAddress,newName, newSurname)
