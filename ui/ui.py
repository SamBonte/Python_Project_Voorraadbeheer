# ui.py

import db.database_manager as db
from models.Drink import Drink
from models.Snack import Snack
from config.settings import DATABASE_TABLE_SNACKS
from config.settings import DATABASE_TABLE_DRINKS

# print to console
def print_table(table_name):
    """Print een tabel (Drinks of Snacks) op de console."""
    if table_name == f"{DATABASE_TABLE_DRINKS}":
        rows = db.get_drinks()
    elif table_name == f"{DATABASE_TABLE_SNACKS}":
        rows = db.get_snacks()
    else:
        raise ValueError(f"Invalid table name. Use {DATABASE_TABLE_DRINKS}' or {DATABASE_TABLE_SNACKS}.")

    print(f"Data from {table_name}:")
    for row in rows:
        print(row)

# save table as csv
def export_data_to_csv(table_name, file_path):
    """Exporteert een tabel naar een CSV-bestand."""
    db.export_to_csv(table_name, file_path)
    print(f"Data from {table_name} has been exported to {file_path}.")

# save table as excel
def export_data_to_excel(table_name, file_path):
    """Exporteert een tabel naar een Excel-bestand."""
    db.export_to_excel(table_name, file_path)
    print(f"Data from {table_name} has been exported to {file_path}.")

def create_drink():
    """Voegt een nieuwe drink toe aan de database"""
    drink_id = input("Geef een ID: ")

    if q_cancel(drink_id):
        return

    if not db.is_valid_id_format(drink_id):
        print("Ongeldig ID-formaat. Het formaat moet zijn XX-0001.")
        return

    # Vraag de andere gegevens op
    name = input("Naam van de drink: ")
    if q_cancel(name):
        return

    unit_price_per_liter = input("Prijs per liter: ")
    if q_cancel(unit_price_per_liter):
        return
    unit_price_per_liter = float(unit_price_per_liter)

    quantity = input("Aantal: ")
    if q_cancel(quantity):
        return
    quantity = int(quantity)

    expiration_date = input("Vervaldatum (DD-MM-YYYY): ")
    if q_cancel(expiration_date):
        return

    # Maak een nieuw Drink object aan
    drink = Drink(unique_id=drink_id,  # Let op dat je unique_id gebruikt, niet id
                  name=name, 
                  unit_price_per_liter=unit_price_per_liter, 
                  quantity=quantity, 
                  expiration_date=expiration_date)

    try:
        db.add_drink(drink)
        print(f"Drink {drink.get_name()} succesvol toegevoegd.")
    except Exception as e:
        print(f"Fout bij het toevoegen van de drink: {e}")


def create_snack():
    """Voegt een nieuwe snack toe aan de database"""
    snack_id = input("Geef een ID: ")

    if q_cancel(snack_id):
        return

    if not db.is_valid_id_format(snack_id):
        print("Ongeldig ID-formaat. Het formaat moet zijn XX-0001.")
        return

    # Vraag de andere gegevens op
    name = input("Naam van de snack: ")
    if q_cancel(name):
        return

    unit_price = input("Prijs per eenheid: ")
    if q_cancel(unit_price):
        return
    unit_price = float(unit_price)

    quantity = input("Aantal: ")
    if q_cancel(quantity):
        return
    quantity = int(quantity)

    expiration_date = input("Vervaldatum (DD-MM-YYYY): ")
    if q_cancel(expiration_date):
        return

    # Maak een nieuw Snack object aan
    snack = Snack(unique_id=snack_id,  # Let op dat je unique_id gebruikt, niet id
                  name=name, 
                  unit_price_per_piece=unit_price, 
                  quantity=quantity, 
                  expiration_date=expiration_date)

    try:
        db.add_snack(snack)
        print(f"Snack {snack.get_name()} succesvol toegevoegd.")
    except Exception as e:
        print(f"Fout bij het toevoegen van de snack: {e}")

# helper function to return to main-menu
def q_cancel(user_input):
    """Controleert of de gebruiker 'q' heeft ingevoerd om een bewerking te annuleren"""
    if user_input == "q":
        return True
    return False