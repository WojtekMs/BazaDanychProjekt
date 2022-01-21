# tutaj scenariusz uzycia:
# - edycja produktu

from sklep.utils import convert_types, pretty_print

from enum import Enum, auto

###############################################################################

def edit_product(cursor, new_quantity, model):
    cursor.execute("""
        UPDATE Produkty
        INNER JOIN Modele ON Produkty.model_id=Modele.model_id
        SET Produkty.ilosc = %s
        WHERE Modele.model = '%s';
""" % (new_quantity, model))


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
