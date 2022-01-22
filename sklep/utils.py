from mysql.connector import FieldType
from tabulate import tabulate
from getpass import getpass

from enum import Enum, auto
class AUTH(Enum):
    ADMIN = auto()
    EMPLOYEE = auto()
    CLIENT = auto()

def convert_types(mysql_rows: list):
    return [tuple(str(item) for item in row) for row in mysql_rows]

def get_headers(description):
    return [col[0] for col in description]

def pretty_print(description: list, rows: list, end='\n'):
    print(tabulate(rows, headers=get_headers(description), tablefmt='psql'), end=end)

def login() -> tuple:
    print("Logowanie")
    username = input("Podaj nazwe uzytkownika: ")
    password = getpass(prompt="Podaj haslo: ")
    return username, password

def get_auth(user: str) -> AUTH:
    if user == "klient":
        return AUTH.CLIENT
    if user == "pracownik":
        return AUTH.EMPLOYEE
    if user == "admin" or user == "root":
        return AUTH.ADMIN
    raise ValueError("bad user")

def is_convertible(value, type):
    try:
        type(value)
        return True
    except ValueError or TypeError:
        return False

def get_typed_input(prompt, type):
    data = input(prompt)
    while not is_convertible(data, type):
        print("Niepoprawne dane!")
        data = input(prompt)
    return type(data)

def get_safe_str_input(prompt):
    data = get_typed_input(prompt, str)
    while "'" in data or '"' in data:
        print("SQL Injection jest zabronione!")
        data = get_typed_input(prompt, str)
    return data