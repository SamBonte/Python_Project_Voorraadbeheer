# database_manager.py

import sys
import os
import sqlite3
from models.Drink import Drink
from models.Snack import Snack

# Voeg de map 'config' toe aan sys.path, zodat Python 'settings.py' kan vinden
sys.path.append(os.path.join(os.path.dirname(__file__), '../config'))

# Importeer de database naam & tabellen uit settings.py
from settings import DATABASE_NAME
from settings import DATABASE_TABLE_SNACKS
from settings import DATABASE_TABLE_DRINKS


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



