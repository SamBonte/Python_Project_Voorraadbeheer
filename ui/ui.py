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

