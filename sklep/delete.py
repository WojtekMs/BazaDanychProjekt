# tutaj scenariusz uzycia:
# - usuwanie produktu
# - usuwanie konta pracownika przez admina
from sklep.utils import convert_types, pretty_print

from enum import Enum, auto


def deleting_product(cursor, model):
    cursor.execute("""
    DELETE Produkty, Modele
    FROM Produkty
    INNER JOIN Modele ON Produkty.model_id=Modele.model_id
    WHERE Modele.model = '%s';
    """ % (model))



