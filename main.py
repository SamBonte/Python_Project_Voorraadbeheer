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
        
        print("0. Afsluiten")
        

        choice = input("Uw keuze: ").strip()

        if choice == '0':
            print("Programma afgesloten. Tot ziens!")
            break

        if choice == '1':
            ui.print_table(f"{DATABASE_TABLE_DRINKS}")
        elif choice == '2':
            ui.print_table(f"{DATABASE_TABLE_SNACKS}")
        else:
            print("Ongeldige keuze. Probeer opnieuw.")


if __name__ == "__main__":
    main()
