from enum import Enum, auto
from sklep.utils import AUTH, get_typed_input

class ACTION(Enum):
    SELECT_PRODUCT = auto()
    ADD_PRODUCT = auto()
    ADD_ORDER = auto()
    ADD_ACCOUNT = auto()
    EDIT_PRODUCT = auto()
    EDIT_ACCOUNT = auto()
    DELETE_PRODUCT = auto()
    DELETE_EMPLOYEE = auto()
    SELECT_EMPLOYEE = auto()
    SELECT_LOGIN_DATA = auto()
    SELECT_CONTACT_DATA = auto()
    SELECT_AUTH = auto()
    QUIT = auto()


class ConsoleView:
    def __init__(self, auth):
        self.auth = auth
        self.action_name = {
            ACTION.SELECT_PRODUCT: "Wyszukaj produkt",
            ACTION.ADD_ORDER: "Złóż zamówienie",
            ACTION.ADD_PRODUCT: "Dodaj produkt",
            ACTION.EDIT_PRODUCT: "Edytuj produkt",
            ACTION.DELETE_PRODUCT: "Usuń produkt",
            ACTION.ADD_ACCOUNT: "Dodaj konto",
            ACTION.EDIT_ACCOUNT: "Edytuj konto",
            ACTION.DELETE_EMPLOYEE: "Usuń konto i dane pracownika",
            ACTION.SELECT_EMPLOYEE: "Wyświetl pracowników",
            ACTION.SELECT_LOGIN_DATA: "Wyświetl dane logowania",
            ACTION.SELECT_CONTACT_DATA: "Wyświetl dane kontaktowe",
            ACTION.SELECT_AUTH: "Wyświetl uprawnienia",
            ACTION.QUIT: "Zakończ"
        }
        self.available_actions = {
            AUTH.CLIENT : [ACTION.SELECT_PRODUCT, ACTION.ADD_ORDER, ACTION.QUIT],
            AUTH.EMPLOYEE : [ACTION.SELECT_PRODUCT, ACTION.ADD_ORDER, ACTION.ADD_PRODUCT, ACTION.EDIT_PRODUCT, ACTION.DELETE_PRODUCT, ACTION.QUIT],
            AUTH.ADMIN : [action for action in ACTION],
        }

    def display_menu(self):
        line = '-' * 100
        print(line)
        for id, action in enumerate(self.available_actions[self.auth]):
            print(f"{id + 1}. {self.action_name[action]}")
        print(line)

    def choose_action(self) -> ACTION:
        actions = self.available_actions[self.auth]
        action_number = get_typed_input("Twój wybór: ", int)
        while action_number < 1 or action_number > len(actions):
            print("Nieprawidłowy wybór!")
            action_number = get_typed_input("Twój wybór: ", int)
        return self.available_actions[self.auth][int(action_number) - 1]
