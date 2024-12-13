# main.py

import ui.ui as ui
import sys
import os
from config.settings import DATABASE_TABLE_SNACKS
from config.settings import DATABASE_TABLE_DRINKS


def main():
    while True:
        print("\nWelkom bij Voorraadbeheer!")
        print("Maak een keuze:")
        print(f"1. Toon de tabel Drinks")
        print(f"2. Toon de tabel Snacks")
        print(f"3. Exporteer Drinks naar een CSV-bestand")
        print(f"4. Exporteer Snacks naar een CSV-bestand")
        print(f"5. Exporteer Drinks naar een Excel-bestand")
        print(f"6. Exporteer Snacks naar een Excel-bestand")
        print("0. Afsluiten")
        

        choice = input("Uw keuze: ").strip()

        if choice == '0':
            print("Programma afgesloten. Tot ziens!")
            break

        if choice == '1':
            ui.print_table(f"{DATABASE_TABLE_DRINKS}")
        elif choice == '2':
            ui.print_table(f"{DATABASE_TABLE_SNACKS}")
        elif choice == '3':
            file_path = input("Geef het pad voor de CSV-export (bv. drinks.csv): ")
            ui.export_data_to_csv(f"{DATABASE_TABLE_DRINKS}", file_path)
        elif choice == '4':
            file_path = input("Geef het pad voor de CSV-export (bv. snacks.csv): ")
            ui.export_data_to_csv(f"{DATABASE_TABLE_SNACKS}", file_path)
        elif choice == '5':
            file_path = input("Geef het pad voor de Excel-export (bv. drinks.xlsx): ")
            ui.export_data_to_excel(f"{DATABASE_TABLE_DRINKS}", file_path)
        elif choice == '6':
            file_path = input("Geef het pad voor de Excel-export (bv. snacks.xlsx): ")
            ui.export_data_to_excel(f"{DATABASE_TABLE_SNACKS}", file_path)
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == "__main__":
    main()
