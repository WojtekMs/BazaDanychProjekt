# tutaj scenariusz uzycia:
# - usuwanie produktu
# - usuwanie konta pracownika przez admina

from sklep.utils import convert_types, pretty_print, get_typed_input, get_safe_str_input

from enum import Enum, auto

###############################################################################

def deleting_product(cursor, model):
    cursor.execute("""
    DELETE Produkty, Modele
    FROM Produkty
    INNER JOIN Modele ON Produkty.model_id=Modele.model_id
    WHERE Modele.model = '%s';
    """ % (model))
    
    
def del_product(cursor, args):
    deleting_product(cursor, args)
    
    
def del_product_get_input():
    print("Usun Produkt\n")
    model = get_safe_str_input("Model urzadzenia: ")
    print()
    return (model)

###############################################################################

def delete_orders(cursor):
    cursor.execute("DELETE FROM zamowienie;")

###############################################################################

def delete_employee(cursor, login):
    cursor.execute(
        "DELETE pracownik, dane_logowania, dane_kontaktowe FROM pracownik " \
        "INNER JOIN dane_logowania ON pracownik.dane_logowania_id=dane_logowania.dane_logowania_id " \
        "INNER JOIN dane_kontaktowe ON pracownik.dane_kontaktowe_id=dane_kontaktowe.dane_kontaktowe_id " \
        f"WHERE dane_logowania.login ='{login}';")
    
    cursor.execute(f"DROP USER IF EXISTS '{login}'@'localhost'")
    
    
def del_employee(cursor, args):
    delete_employee(cursor, args)
    
    
def del_employee_get_input():
    print("Usun Konto\n")
    login = get_safe_str_input("Login Pracownika: ")
    print()
    return (login)
