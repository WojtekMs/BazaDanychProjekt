import mysql.connector
from mysql.connector.errors import ProgrammingError

from tabulate import tabulate
from getpass import getpass

from enum import Enum, auto


class AUTH(Enum):
    ADMIN = auto()
    EMPLOYEE = auto()
    CLIENT = auto()


class AuthError(Exception):

    def __init__(self):
        super().__init__(
            "User does not have any of the following roles: 'admin', 'pracownik', 'klient'"
        )


def convert_types(mysql_rows: list):
    return [tuple(str(item) for item in row) for row in mysql_rows]


def get_headers(description):
    return [col[0] for col in description]


def pretty_print(description: list, rows: list, end='\n'):
    print(tabulate(rows, headers=get_headers(description), tablefmt='pretty'),
          end=end)


def login(login_prompt="Podaj nazwe uzytkownika: ",
          password_prompt="Podaj haslo: ") -> tuple:
    username = get_safe_str_input(login_prompt)
    password = getpass(prompt=password_prompt)
    return username, password


def get_auth(cursor, user: str) -> AUTH:
    if user == 'klient':
        return AUTH.CLIENT
    description, rows = execute_query(
        cursor, f"SHOW GRANTS FOR '{user}'@'localhost';")
    for row in rows:
        if row[0].startswith('GRANT `admin`'):
            return AUTH.ADMIN
        if row[0].startswith('GRANT `pracownik`'):
            return AUTH.EMPLOYEE
    raise AuthError()


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


def choose_one_of(actions: list):
    for action in actions:
        print(action)
    action_number = get_typed_input("Twój wybór: ", int)
    while action_number < 1 or action_number > len(actions):
        print("Nieprawidłowy wybór!")
        action_number = get_typed_input("Twój wybór: ", int)
    return actions[action_number - 1]


def execute_query(cursor, query: str):
    cursor.execute(query)
    rows = cursor.fetchall()
    rows = convert_types(rows)
    return cursor.description, rows


def connect(user, password, db):
    conn = mysql.connector.connect(host='localhost',
                                       user=user,
                                       password=password,
                                       port=3306,
                                       database=db,
                                       buffered=True,
                                       raw=False)
    return conn
