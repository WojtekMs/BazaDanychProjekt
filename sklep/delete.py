# tutaj scenariusz uzycia:
# - usuwanie produktu
# - usuwanie konta pracownika przez admina

def delete_orders(cursor):
    cursor.execute("DELETE FROM zamowienie;")


def delete_employee(cursor, employee_id):
    cursor.execute(f"DELETE FROM dane_logowania WHERE dane_logowania_id IN (SELECT dane_logowania_id FROM pracownik WHERE pracownik_id={employee_id});")
    cursor.execute(f"DELETE FROM dane_kontaktowe WHERE dane_kontaktowe_id IN (SELECT dane_kontaktowe_id FROM pracownik WHERE pracownik_id={employee_id});")
    cursor.execute(f"DELETE FROM pracownik WHERE pracownik_id={employee_id};")
