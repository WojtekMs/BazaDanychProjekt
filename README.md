# Baza Danych Projekt

## Quick Start Windows
Upewnij sie ze posiadasz zainstalowanego pythona!

1. uruchom cmd i przejdz do katalogu gdzie jest repozytorium gita  
`cd C:\Users....`

2. utworz srodowisko wirtualne w repozytorium  
`python -m venv venv-win`

3. aktywuj srodowisko wirtualne  
`venv-win\Scripts\activate.bat`

4. pobierz wymagane paczki  
`pip install -r requirements.txt`  
`pip install -e .`

5. uruchom serwer MySQL (mozesz to zrobic za pomoca MySQL Workbench)


6. uruchom interface.py podajac nazwe swojej bazy danych, ktora utworzyles w MySQLWorkbench (np. sklep, sklep_rtv;)  
`python interface.py <db>`

Jesli wszystko sie powiodlo to powinien Ci sie wyswietlic ekran logowania.

