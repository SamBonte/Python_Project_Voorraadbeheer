import re
from datetime import datetime

class Drink:
    """Aanmaken van een Drink-object met controle"""
    def __init__(self, unique_id, name, unit_price_per_liter, quantity, expiration_date):

        # Controle op unique_id
        if type(unique_id) == str and self._validate_unique_id(unique_id):
            self._unique_id = unique_id
        else:
            raise ValueError(f"Invalid value {unique_id} for: unique_id. Must match format 'XX-0001'.")

        # Controle op name
        if type(name) == str:
            self._name = name
        else:
            raise TypeError(f"Invalid value {name} for: name. Must be a string.")

        # Controle op unit_price_per_liter
        if type(unit_price_per_liter) in [int, float] and unit_price_per_liter > 0:
            self._unit_price_per_liter = round(unit_price_per_liter, 2)
        else:
            raise ValueError(f"Invalid value {unit_price_per_liter} for: unit_price_per_liter. Must be a positive number.")

        # Controle op quantity
        if type(quantity) == int and quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError(f"Invalid value {quantity} for: quantity. Must be a positive integer.")

        # Controle op expiration_date
        if type(expiration_date) == str and self._validate_date(expiration_date):
            self._expiration_date = expiration_date
        else:
            raise ValueError(f"Invalid value {expiration_date} for: expiration_date. Must match format 'DD-MM-YYYY'.")

    # Getters
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

    # Setters
    def set_name(self, name):
        if type(name) == str:
            self._name = name
        else:
            raise TypeError(f"Invalid value {name} for: name. Must be a string.")

    def set_unit_price_per_liter(self, unit_price_per_liter):
        if type(unit_price_per_liter) in [int, float] and unit_price_per_liter > 0:
            self._unit_price_per_liter = round(unit_price_per_liter, 2)
        else:
            raise ValueError(f"Invalid value {unit_price_per_liter} for: unit_price_per_liter. Must be a positive number.")

    def set_quantity(self, quantity):
        if type(quantity) == int and quantity >= 0:
            self._quantity = quantity
        else:
            raise ValueError(f"Invalid value {quantity} for: quantity. Must be a positive integer.")

    def add_quantity(self, add_amount, sign):
        if type(add_amount) == int:
            if sign == "+":
                self._quantity += add_amount
            elif sign == "-" and (self._quantity - add_amount) >= 0:
                self._quantity -= add_amount
            else:
                raise ValueError(f"Invalid operation: sign=['+' or '-'] and resulting quantity must be non-negative.")
        else:
            raise ValueError(f"Invalid value {add_amount} for: add_amount. Must be a positive integer.")

    def __str__(self):
        return (f"Drink Information:\n"
                f"  ID:               {self._unique_id}\n"
                f"  Name:             {self._name}\n"
                f"  Unit Price/L (€): {self._unit_price_per_liter:.2f}\n"
                f"  Quantity:         {self._quantity}\n"
                f"  Expiration Date:  {self._expiration_date}")

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
        
