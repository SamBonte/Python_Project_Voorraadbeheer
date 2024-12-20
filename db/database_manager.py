# database_manager.py

import sys
import os
import sqlite3
from models.Drink import Drink
from models.Snack import Snack

import csv
from openpyxl import Workbook # Moet in requirements.txt komen

# Voeg de map 'config' toe aan sys.path, zodat Python 'settings.py' kan vinden
sys.path.append(os.path.join(os.path.dirname(__file__), '../config'))

# Importeer de database naam & tabellen uit settings.py
from settings import DATABASE_NAME
from settings import DATABASE_TABLE_SNACKS
from settings import DATABASE_TABLE_DRINKS
from settings import PASSWORD_ADMIN


def connect_to_db():
    """Verbindt met de database gedefinieerd in settings.py"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except sqlite3.Error as e:
        raise Exception(f"Error connecting to database: {e}")

def get_drinks():
    """Retourneert alle rijen uit de tabel Drinks"""
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {DATABASE_TABLE_DRINKS}")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_snacks():
    """Retourneert alle rijen uit de tabel Snacks"""
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {DATABASE_TABLE_SNACKS}")
    rows = cursor.fetchall()
    conn.close()
    return rows

def export_to_csv(table_name, file_path):
    """Exporteert een tabel (Drinks of Snacks) naar een CSV-bestand"""
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    conn.close()

    import csv
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

def export_to_excel(table_name, file_path):
    """Exporteert een tabel (Drinks of Snacks) naar een Excel-bestand"""
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    conn.close()

    workbook = Workbook()
    sheet = workbook.active
    sheet.append(headers)
    for row in rows:
        sheet.append(row)
    workbook.save(file_path)

# controls validity unique_id
def is_valid_id_format(id):
    """Controleert of een ID voldoet aan het formaat XX-0001"""
    import re
    return bool(re.match(r'^[A-Z]{2}-\d{4}$', id))

# searches db
def id_exists(table_name, unique_id):
    """Controleert of een gegeven ID al in de tabel aanwezig is"""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT unique_id FROM {table_name} WHERE unique_id = ?", (unique_id,))
        return cursor.fetchone() is not None
    except sqlite3.Error as e:
        raise Exception(f"Error checking ID existence: {e}")
    finally:
        conn.close()

# provides user with possible unique_id number
def get_next_id(table_name):
    """Berekent het eerstvolgende geldige ID voor de gegeven tabel"""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT MAX(unique_id) FROM {table_name}")
        result = cursor.fetchone()[0]
        if result:
            prefix, num = result.split('-')
            next_id = f"{prefix}-{int(num) + 1:04d}"
        else:
            # Begin met het eerste ID
            next_id = f"{table_name[:2].upper()}-0001"
    except sqlite3.Error as e:
        raise Exception(f"Error retrieving next ID: {e}")
    finally:
        conn.close()
    return next_id

# adds drink to db
def add_drink(drink):
    """Voegt een Drink-object toe aan de tabel Drinks"""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        
        if id_exists("Drinks", drink.get_unique_id()):
            raise Exception(f"Drink met ID '{drink.get_unique_id()}' bestaat al. Eerstvolgende geldige ID: {get_next_id('Drinks')}")
        
        cursor.execute(
            "INSERT INTO Drinks (unique_id, name, unit_price_per_liter, quantity, expiration_date) VALUES (?, ?, ?, ?, ?)",
            (drink.get_unique_id(), drink.get_name(), drink.get_unit_price_per_liter(), drink.get_quantity(), drink.get_expiration_date()),
        )
        conn.commit()
    except sqlite3.Error as e:
        raise Exception(f"Error inserting drink: {e}")
    finally:
        conn.close()

# adds snack to db
def add_snack(snack):
    """Voegt een Snack-object toe aan de tabel Snacks"""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        # Controleer of de Snack al bestaat op basis van unique_id
        if id_exists("Snacks", snack.get_unique_id()): 
            raise Exception(f"Snack met ID '{snack.get_unique_id()}' bestaat al. Eerstvolgende geldige ID: {get_next_id('Snacks')}")
        
        cursor.execute(
            "INSERT INTO Snacks (unique_id, name, unit_price, quantity, expiration_date) VALUES (?, ?, ?, ?, ?)",
            (snack.get_unique_id(), snack.get_name(), snack.get_unit_price_per_piece(), snack.get_quantity(), snack.get_expiration_date()),
        )
        conn.commit()
    except sqlite3.Error as e:
        raise Exception(f"Error inserting snack: {e}")
    finally:
        conn.close()

# gets drink from db
def get_drink_by_id(drink_id):
    """Haalt een drink op uit de database op basis van unique_id"""
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {DATABASE_TABLE_DRINKS} WHERE unique_id = ?", (drink_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        # Retourneer een Drink object
        return Drink(row[0], row[1], row[2], row[3], row[4])  # row[0] = unique_id, row[1] = name, etc.
    else:
        raise Exception(f"Drink met ID '{drink_id}' niet gevonden.")

# gets snack from db
def get_snack_by_id(snack_id):
    """Haalt een snack op uit de database op basis van unique_id"""
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {DATABASE_TABLE_SNACKS} WHERE unique_id = ?", (snack_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        # Retourneer een Snack object
        return Snack(row[0], row[1], row[2], row[3], row[4])  # row[0] = unique_id, row[1] = name, etc.
    else:
        raise Exception(f"Snack met ID '{snack_id}' niet gevonden.")

# update/modifies drink
def update_drink(drink):
    """Werk de drinkgegevens bij in de database"""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE Drinks SET name = ?, unit_price_per_liter = ?, quantity = ?, expiration_date = ? WHERE unique_id = ?",
            (drink.get_name(), drink.get_unit_price_per_liter(), drink.get_quantity(), drink.get_expiration_date(), drink.get_unique_id())
        )
        conn.commit()
    except sqlite3.Error as e:
        raise Exception(f"Error updating drink: {e}")
    finally:
        conn.close()

# updates/modifies snack
def update_snack(snack):
    """Werk de snackgegevens bij in de database"""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE Snacks SET name = ?, unit_price = ?, quantity = ?, expiration_date = ? WHERE unique_id = ?",
            (snack.get_name(), snack.get_unit_price_per_piece(), snack.get_quantity(), snack.get_expiration_date(), snack.get_unique_id())
        )
        conn.commit()
    except sqlite3.Error as e:
        raise Exception(f"Error updating snack: {e}")
    finally:
        conn.close()

# deletes dring from db
def delete_drink_by_id(drink_id):
    """Verwijdert een drink uit de database op basis van unique_id"""
    conn = connect_to_db()
    cursor = conn.cursor()
    
    try:
        password = input("Password admin to confirm: ");
        if password == f"{PASSWORD_ADMIN}":
            cursor.execute(f"DELETE FROM {DATABASE_TABLE_DRINKS} WHERE unique_id = ?", (drink_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise Exception(f"Drink met ID '{drink_id}' niet gevonden.")
            else:
                print(f"Drink met ID '{drink_id}' succesvol verwijderd.")
        else:
            print(f"Access denied")
        

    except sqlite3.Error as e:
        raise Exception(f"Fout bij het verwijderen van de snack: {e}")
    finally:
        conn.close()

# deletes snack from db
def delete_snack_by_id(snack_id):
    """Verwijdert een snack uit de database op basis van unique_id"""
    conn = connect_to_db()
    cursor = conn.cursor()
    try:
        password = input("Password admin to confirm: ");
        if password == f"{PASSWORD_ADMIN}":
            cursor.execute(f"DELETE FROM {DATABASE_TABLE_SNACKS} WHERE unique_id = ?", (snack_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise Exception(f"Snack met ID '{snack_id}' niet gevonden.")
            else:
                print(f"Snack met ID '{snack_id}' succesvol verwijderd.")
        else:
            print(f"Access denied")
        

    except sqlite3.Error as e:
        raise Exception(f"Fout bij het verwijderen van de snack: {e}")
    finally:
        conn.close()