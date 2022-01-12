from sklep.utils import convert_types

from enum import Enum, auto

class Operand(Enum):
    LESS = auto()
    GREATER = auto()
    EQUAL = auto()

def select_product_by_price(cursor, price_threshold: float, operand: Operand):
    if operand == Operand.LESS:
        cursor.execute(
            f"SELECT * FROM Produkty WHERE cena < {price_threshold};")
    if operand == Operand.GREATER:
        cursor.execute(
            f"SELECT * FROM Produkty WHERE cena > {price_threshold};")
    if operand == Operand.EQUAL:
        cursor.execute(f"SELECT * FROM Produkty WHERE cena={price_threshold};")
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows


def select_product_between_prices(cursor, min_price: float, max_price: float):
    cursor.execute(
        f"SELECT * FROM Produkty WHERE cena > {min_price} AND cena < {max_price};"
    )
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows
