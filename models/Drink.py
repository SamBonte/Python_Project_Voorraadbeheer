# Drink.py

import sys
import re
from datetime import datetime

class Drink:
    """Aanmaken van een Snack-object met controle"""
    def __init__(self, unique_id, name, unit_price_per_liter, quantity, expiration_date):

        # Controle op unique_id
        if type(unique_id) == str and self._validate_unique_id(unique_id):
            self._unique_id = unique_id
        else:
            print("Invalid value for: unique_id. Must match format 'XX-0001'.")
            sys.exit(-1)

        # Controle op name
        if type(name) == str:
            self._name = name
        else:
            print("Invalid value for: name. Must be a string.")
            sys.exit(-1)

        # Controle op unit_price_per_liter
        if type(unit_price_per_liter) in [int, float] and unit_price_per_liter > 0:
            self._unit_price_per_liter = round(unit_price_per_liter, 2)
        else:
            print("Invalid value for: unit_price_per_liter. Must be a positive number.")
            sys.exit(-1)

        # Controle op quantity
        if type(quantity) == int and quantity >= 0:
            self._quantity = quantity
        else:
            print("Invalid value for: quantity. Must be a non-negative integer.")
            sys.exit(-1)

        # Controle op expiration_date
        if type(expiration_date) == str and self._validate_date(expiration_date):
            self._expiration_date = expiration_date
        else:
            print("Invalid value for: expiration_date. Must match format 'DD-MM-YYYY'.")
            sys.exit(-1)

    def get_unique_id(self):
        return self._unique_id

    def get_name(self):
        return self._name

    def get_unit_price_per_liter(self):
        return self._unit_price_per_liter

    def get_quantity(self):
        return self._quantity

    def get_expiration_date(self):
        return self._expiration_date

    def printSnack(self):
        print(f"--<Drink Information>--")
        print(f"  ID:               {self._unique_id}")
        print(f"  Name:             {self._name}")
        print(f"  Unit Price (€):   {self._unit_price_per_liter:.2f}")
        print(f"  Quantity:         {self._quantity}")
        print(f"  Expiration Date:  {self._expiration_date}")
        print(f"--------<>--------")

    @staticmethod
    def _validate_unique_id(unique_id):
        """Controleert het formaat van unique_id"""
        return bool(re.fullmatch(r"[A-Z]{2}-\d{4}", unique_id))

    @staticmethod
    def _validate_date(date_string):
        """Controleert het formaat van de datum"""
        try:
            datetime.strptime(date_string, "%d-%m-%Y")
            return True
        except ValueError:
            return False
