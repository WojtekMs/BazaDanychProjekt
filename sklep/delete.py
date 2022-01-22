# tutaj scenariusz uzycia:
# - usuwanie produktu
# - usuwanie konta pracownika przez admina

from sklep.utils import convert_types, pretty_print

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
    deleting_product(cursor, args[0])
    
    
def del_product_get_input():
    print("Usun produkt\n")
    model = get_safe_str_input("Model urzadzenia: ")
    print()
    return (model)

###############################################################################

def delete_orders(cursor):
    cursor.execute("DELETE FROM zamowienie;")

###############################################################################

def delete_employee(cursor, employee_id):
    cursor.execute(f"DELETE FROM dane_logowania WHERE dane_logowania_id IN (SELECT dane_logowania_id FROM pracownik WHERE pracownik_id={employee_id});")
    cursor.execute(f"DELETE FROM dane_kontaktowe WHERE dane_kontaktowe_id IN (SELECT dane_kontaktowe_id FROM pracownik WHERE pracownik_id={employee_id});")
    cursor.execute(f"DELETE FROM pracownik WHERE pracownik_id={employee_id};")
