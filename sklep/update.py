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
    