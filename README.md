# Baza Danych Projekt

## Quick Start Windows
Upewnij sie ze posiadasz zainstalowanego pythona!

1. uruchom cmd i przejdz do katalogu gdzie jest repozytorium gita
`cd C:\Users....`

2. utworz srodowisko wirtualne w repozytorium
`python -m venv venv`

3. aktywuj srodowisko wirtualne
`venv-win\Scripts\activate.bat`

4. pobierz wymagane paczki
`pip install -r requirements.txt`

5. uruchom serwer MySQL (mozesz to zrobic za pomoca MySQL Workbench)

6. dodaj swoje haslo dla uzytkownika root w bazie danych do zmiennej srodowiskowej
`set MYSQL_PASS=<twoje_haslo>`

7. uruchom interface.py podajac nazwe swojej bazy danych, ktora utworzyles w MySQLWorkbench (np. sklep, sklep_rtv;)
`python interface.py <db>`

Jesli wszystko sie powiodlo to powinno Ci sie wyswietlic cos w tym stylu:
```sql
((1, 'Admin\r'),)  
((2, 'Pracownik\r'),)  
((31, 'admin'),)
```

