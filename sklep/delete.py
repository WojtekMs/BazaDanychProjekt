# tutaj scenariusz uzycia:
# - usuwanie produktu
# - usuwanie konta pracownika przez admina

def delete_orders(cursor):
    cursor.execute("DELETE FROM zamowienie;")
