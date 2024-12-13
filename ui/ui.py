# ui.py

import db.database_manager as db
from models.Drink import Drink
from models.Snack import Snack
from config.settings import DATABASE_TABLE_SNACKS
from config.settings import DATABASE_TABLE_DRINKS


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
