# Voorraadbeheer

[![standard-readme compliant](https://img.shields.io/badge/VoorraadBeheer-Home-brightgreen.svg?style=flat-square)](https://github.com/SamBonte/Python_Project_Voorraadbeheer)

**Voorraadbeheer** is een Python-applicatie voor het beheren van voorraad van drank- en snackproducten. De applicatie maakt gebruik van een SQLite-database voor het opslaan van productinformatie en biedt een eenvoudige gebruikersinterface voor het beheren van deze voorraad. De applicatie biedt functionaliteiten zoals het tonen van voorraadtabellen, het toevoegen, bijwerken en verwijderen van producten, en het exporteren van gegevens naar CSV- of Excel-bestanden.

## Inhoud
- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [Bestandenstructuur](#bestandenstructuur)
- [Afhankelijkheden](#afhankelijkheden)
- [Toekomstige verbeteringen](#toekomstige-verbeteringen)

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

3. **Clone het project in de virtuele omgeving: Clone nu het project naar je lokale machine:**

```bash
git clone https://github.com/SamBonte/Python_Project_Voorraadbeheer.git
```

4. **Installeer de vereiste afhankelijkheden: Ga naar de projectmap en installeer de benodigde pakketten:**

```bash
cd Voorraadbeheer
pip install -r requirements.txt
```


5. **Initialiseer de testdatabase: Om de applicatie te kunnen gebruiken, moet je eerst de testdatabase aanmaken. Dit kan door het volgende script uit te voeren:**

```bash
python ./db/create_testdb.py
```


5.5 **Verbind je eigen Voorraad-database/de testdatabase (optioneel): Als je een eigen voorraad-database wilt gebruiken in plaats van de testdatabase, kun je de databaseverbinding configureren in het bestand settings.py in de config map.**

Maak een settings.py bestand aan in de config map en definieer de volgende variabelen:

```python
DATABASE_NAME = "pad/naar/jouw/database.db" of "db/voorraad.db"
DATABASE_TABLE_SNACKS = "Snacks"
DATABASE_TABLE_DRINKS = "Drinks"
PASSWORD_ADMIN = "admin"  # Pas dit aan indien gewenst
```

Zorg ervoor dat je de juiste padnaam opgeeft voor je eigen databasebestand. Het standaardpad voor de testdatabase is db/voorraad.db.

## Gebruik

Nadat de installatie goed gebeurd is: (test database voorraad.db aanwezig in de db folder, settings.py gedefinieerd)

1. **Run de applicatie (current directory on cmd = yourPath/Voorraadbeheer)**
   ```bash
  python ./main.py
   ```
Na het starten van de applicatie kun je kiezen uit verschillende opties om de voorraad van drank- en snackproducten te beheren. Dit zijn de hoofdopties:

2. **Je drukt het nummer/letter**
  1 -> Toon de tabel Drinks - Weergave van alle drankproducten in de database.
  2 -> Toon de tabel Snacks - Weergave van alle snackproducten in de database.
  3 -> Exporteer Drinks naar CSV - Exporteer de drankproducten naar een CSV-bestand.
  4 -> Exporteer Snacks naar CSV - Exporteer de snackproducten naar een CSV-bestand.
  5 -> Exporteer Drinks naar Excel - Exporteer de drankproducten naar een Excel-bestand.
  6 -> Exporteer Snacks naar Excel - Exporteer de snackproducten naar een Excel-bestand.
  7 -> Voeg een nieuwe Drink toe - Voeg een nieuw drankproduct toe.
  8 -> Voeg een nieuwe Snack toe - Voeg een nieuw snackproduct toe.
  9 -> Wijzig een bestaande Drink - Wijzig gegevens van een bestaand drankproduct.
  10 -> Wijzig een bestaande Snack - Wijzig gegevens van een bestaand snackproduct.
  11 -> Verwijder een Drink - Verwijder een bestaand drankproduct.
  12 -> Verwijder een Snack - Verwijder een bestaand snackproduct.
  0 -> Afsluiten - Sluit de applicatie af.
  q -> Om een actie te stoppen



[@SamBonte](https://github.com/SamBonte).
