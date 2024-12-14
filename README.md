# Voorraadbeheer

[![standard-readme compliant](https://img.shields.io/badge/VoorraadBeheer-Home-brightgreen.svg?style=flat-square)](https://github.com/SamBonte/Python_Project_Voorraadbeheer)

**Voorraadbeheer** is een Python-applicatie voor het beheren van voorraad van drank- en snackproducten. De applicatie maakt gebruik van een SQLite-database voor het opslaan van productinformatie en biedt een eenvoudige gebruikersinterface voor het beheren van deze voorraad. De applicatie biedt functionaliteiten zoals het tonen van voorraadtabellen, het toevoegen, bijwerken en verwijderen van producten, en het exporteren van gegevens naar CSV- of Excel-bestanden.

## Inhoud
- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [Bestandenstructuur](#bestandenstructuur)
- [Afhankelijkheden](#afhankelijkheden)
- [Structuur van de Voorraad Database](#structuur-van-de-voorraad-database)


## Installatie

Volg de onderstaande stappen om **Voorraadbeheer** lokaal op te zetten in een virtuele omgeving:

1. **Maak een virtuele omgeving aan**:
   Voordat je begint, moet je een virtuele omgeving maken voor dit project. Open een terminal of opdrachtprompt en voer de volgende opdracht uit:
   ```bash
   python -m venv .venv
   ```
2. **Activeer de virtuele omgeving: Activeer de virtuele omgeving afhankelijk van je besturingssysteem:**

Voor Windows:
  ```bash
 ".venv\Scripts\activate"
  ```
Voor macOS/Linux:
```bash
source .venv/bin/activate
```

**OPM: Als u zich uit de .venv omgeving wilt begeven typ dan het volgende commando:**

```bash
deactivate
```

3. **Clone het project in de virtuele omgeving: Clone nu het project naar je lokale machine:**

```bash
git clone https://github.com/SamBonte/Python_Project_Voorraadbeheer.git
```

4. **Installeer de vereiste afhankelijkheden: Ga naar de projectmap en installeer de benodigde pakketten:**

```bash
cd Python_Project_Voorraadbeheer
pip install -r requirements.txt
```

5. **Verbind je eigen Voorraad-database/de testdatabase (optioneel):**\
   (Als je een eigen voorraad-database wilt gebruiken in plaats van de testdatabase, kun je de databaseverbinding configureren in het bestand settings.py in de config map.)

Maak een settings.py bestand aan in de config map:
```python
python -c "open('config/settings.py', 'w').close()"
```

- Open verkenner en navigeer naar de Project_Voorraadbeheer folder.
- Navigeer naar de config folder.
- Rechts klik op de settings.py.
- Kies voor de optie *Bewerken in Notepad*
- Kopiëer de volgende variabelen in de setttings.py file:

```python
DATABASE_NAME = "pad/naar/jouw/database.db" of "db/voorraad.db"
DATABASE_TABLE_SNACKS = "Snacks"
DATABASE_TABLE_DRINKS = "Drinks"
PASSWORD_ADMIN = "admin"  # Pas dit aan indien gewenst
```
- Vergeet niet de wijzigingen in de settings.py file te saven.\

Zorg ervoor dat je de juiste padnaam opgeeft voor je eigen databasebestand. Het standaardpad voor de testdatabase is db/voorraad.db.

6. **Initialiseer de testdatabase:**

In de terminal ben je nog steeds in de Python_Project_Voorraadbeheer folder
```bash
C:\YourPath\Python_Project_Voorraadbeheer>
```

Om de applicatie te kunnen gebruiken, moet je eerst de testdatabase aanmaken. Dit kan door het volgende script uit te voeren:

```bash
python ./db/create_test_db.py
```

## Gebruik


Nadat de installatie goed gebeurd is: (test database voorraad.db aanwezig in de db folder, settings.py gedefinieerd)

1. **Run de applicatie (current directory on cmd = yourPath/Voorraadbeheer)**

   ```python
   python ./main.py
   ```

Na het starten van de applicatie kun je kiezen uit verschillende opties om de voorraad van drank- en snackproducten te beheren. Dit zijn de hoofdopties:

2. **Je drukt het nummer/letter:**
   
   1 -> Toon de tabel Drinks - Weergave van alle drankproducten in de database.\
   2 -> Toon de tabel Snacks - Weergave van alle snackproducten in de database.\
   3 -> Exporteer Drinks naar CSV - Exporteer de drankproducten naar een CSV-bestand.\
   4 -> Exporteer Snacks naar CSV - Exporteer de snackproducten naar een CSV-bestand.\
   5 -> Exporteer Drinks naar Excel - Exporteer de drankproducten naar een Excel-bestand.\
   6 -> Exporteer Snacks naar Excel - Exporteer de snackproducten naar een Excel-bestand.\
   7 -> Voeg een nieuwe Drink toe - Voeg een nieuw drankproduct toe.\
   8 -> Voeg een nieuwe Snack toe - Voeg een nieuw snackproduct toe.\
   9 -> Wijzig een bestaande Drink - Wijzig gegevens van een bestaand drankproduct.\
   10 -> Wijzig een bestaande Snack - Wijzig gegevens van een bestaand snackproduct.\
   11 -> Verwijder een Drink - Verwijder een bestaand drankproduct.\
   12 -> Verwijder een Snack - Verwijder een bestaand snackproduct.\
   0 -> Afsluiten - Sluit de applicatie af.\
   q -> Om een actie te stoppen.
   
**OPM: Bij het verwijderen wordt een wachtwoord gevraagt, deze stelde je in op
       *admin* of *je zelf gekozen passwoord* in de settings.py file.**
       
Default paswoord:
```bash
C:/YourPath/Python_Project_Voorraadbeheer>Password admin to confirm: admin
```

**OPM: Bij het exporteren naar CSV/Excel wordt een pad gevraagt, deze kan in de folder zelf of op een zelfgekozen locatie:**

In de folder zelf:
```bash
C:/YourPath/Python_Project_Voorraadbeheer>Geef een pad op (bv. drinks.csv): ./drinks.csv
```

In een zelfgekozen pad "p":
```bash
C:/YourPath/Python_Project_Voorraadbeheer>Geef een pad op (bv. drinks.xlsx): p/drinks.csv
```

## Bestandenstructuur
De projectstructuur is als volgt:

```markdown

C:.
│   .gitignore
│   main.py
│   README.md
│   requirements.txt
│
├───config
│   │   settings.py
│   │
│   └───__pycache__
│           settings.cpython-312.pyc
│
├───db
│   │   create_test_db.py
│   │   database_manager.py
│   │   voorraad.db
│   │
│   └───__pycache__
│           database_manager.cpython-312.pyc
│
├───models
│   │   Drink.py
│   │   Snack.py
│   │   
│   │
│   └───__pycache__
│           Drink.cpython-312.pyc
│           Snack.cpython-312.pyc
│
└───ui
    │   ui.py
    │
    └───__pycache__
            ui.cpython-312.pyc
```
- config/: Bevat configuratie-instellingen zoals de databaseverbinding en wachtwoorden.
  - settings.py: Instellingen voor de database en andere globale variabelen.

- db/: Bevat de databasebestanden (SQLite).

  - voorraad.db: De SQLite-database waar de voorraad van drank- en snackproducten wordt opgeslagen.
  - Het create_test_db.py script: Een Python-script om de testdatabase te initialiseren.

- models/: Bevat de modelklassen voor de drank- en snackobjecten.
  
   - drink.py: Bevat de klasse voor drankproducten, inclusief validatie en methoden.
   - snack.py: Bevat de klasse voor snackproducten, inclusief validatie en methoden.

- ui/: Bevat de gebruikersinterface-methoden voor het tonen van tabellen, toevoegen, bewerken en verwijderen van producten.
  
   - ui.py: Bevat methoden zoals print_table, create_drink, create_snack, enzovoort.

## Afhankelijkheden
1. **Het project heeft de volgende Python-pakketten nodig:**

- sqlite3: Voor database-interacties.
- pandas: Voor export naar CSV en Excel-bestanden.
- openpyxl: Voor export naar Excel-bestanden.

2. **Je hebt de afhankelijkheden geïnstalleerd via:**

```bash
pip install -r requirements.txt
```

## Structuur van de Voorraad Database

Om de **Voorraadbeheer** applicatie correct te laten werken, moet de voorraad-database voldoen aan een specifieke structuur. De database bestaat uit twee hoofdtabellen: **Drinks** en **Snacks**. Elke tabel moet een aantal noodzakelijke velden bevatten, die hieronder worden beschreven.

### 0. **Opmerkingen**
- Het unique_id veld wordt in verschillende scripts gecontroleert op het formaat "XX-0000".
- De expiration_date wordt in verschillende scripts gecontroleert op het formaat "DD-MM-YYYY".
- Het veld unit_price in de database, komt overeen met de variabele unit_price_per_piece in de klasse Snack.
- Het veld unit_price in de database, komt overeen met de variabele unit_price_per_liter in de klasse Drink.

### 1. **Drinks Tabel**
De **Drinks** tabel bevat informatie over drankproducten. De velden in deze tabel moeten als volgt zijn:

- **unique_id** (TEXT): Een unieke identificatie voor het drankproduct. Dit veld moet een string zijn in het formaat `XX-0001`, waarbij `XX` twee letters zijn en `0001` een viercijferig nummer.
- **name** (TEXT): De naam van het drankproduct.
- **unit_price_per_liter** (REAL): De prijs per liter van de drank (bijvoorbeeld 2.50 voor €2,50 per liter).
- **quantity** (INTEGER): Het aantal eenheden van het drankproduct in de voorraad.
- **expiration_date** (TEXT): De vervaldatum van het product, geformatteerd als `DD-MM-YYYY`.

### 2. **Snacks Tabel**
De **Snacks** tabel bevat informatie over snackproducten. De velden in deze tabel moeten als volgt zijn:

- **unique_id** (TEXT): Een unieke identificatie voor het snackproduct. Dit veld moet een string zijn in het formaat `XX-0001`, waarbij `XX` twee letters zijn en `0001` een viercijferig nummer.
- **name** (TEXT): De naam van het snackproduct.
- **unit_price_per_piece** (REAL): De prijs per stuk van de snack (bijvoorbeeld 1.50 voor €1,50 per stuk).
- **quantity** (INTEGER): Het aantal eenheden van het snackproduct in de voorraad.
- **expiration_date** (TEXT): De vervaldatum van het product, geformatteerd als `DD-MM-YYYY`.

### 3. **Voorbeeld Database Schema**
Het onderstaande SQL-schema toont een voorbeeld van hoe een werkende Voorraad database eruit moet zien:

```sql
CREATE TABLE Drinks (
    unique_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    unit_price_per_liter REAL NOT NULL,
    quantity INTEGER NOT NULL,
    expiration_date TEXT NOT NULL
);

CREATE TABLE Snacks (
    unique_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    unit_price_per_piece REAL NOT NULL,
    quantity INTEGER NOT NULL,
    expiration_date TEXT NOT NULL
);
```


[@SamBonte](https://github.com/SamBonte).
