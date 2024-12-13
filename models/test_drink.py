import unittest
from datetime import datetime
from Drink import Drink

class TestDrink(unittest.TestCase):
    
    def test_valid_drink_creation(self):
        """Test scenario voor een geldig Drink-object."""
        drink = Drink("XX-0001", "Spa water", 0.5, 6, "13-10-2026")
        self.assertEqual(drink.get_unique_id(), "XX-0001")
        self.assertEqual(drink.get_name(), "Spa water")
        self.assertEqual(drink.get_unit_price_per_liter(), 0.5)
        self.assertEqual(drink.get_quantity(), 6)
        self.assertEqual(drink.get_expiration_date(), "13-10-2026")

    def test_invalid_unique_id(self):
        """Test een ongeldige unieke ID."""
        with self.assertRaises(ValueError):
            Drink("X-001", "Spa water", 0.5, 6, "13-10-2026")

    def test_invalid_name(self):
        """Test een ongeldige naam."""
        with self.assertRaises(TypeError):
            Drink("XX-0001", 123, 0.5, 6, "13-10-2026")

    def test_invalid_unit_price(self):
        """Test een ongeldige eenheidsprijs."""
        with self.assertRaises(ValueError):
            Drink("XX-0001", "Spa water", -0.5, 6, "13-10-2026")

        with self.assertRaises(ValueError):
            Drink("XX-0001", "Spa water", "prijs", 6, "13-10-2026")

    def test_invalid_quantity(self):
        """Test een ongeldige hoeveelheid."""
        with self.assertRaises(ValueError):
            Drink("XX-0001", "Spa water", 0.5, -1, "13-10-2026")

    def test_invalid_expiration_date(self):
        """Test een ongeldige vervaldatum."""
        with self.assertRaises(ValueError):
            Drink("XX-0001", "Spa water", 0.5, 6, "13/10/2026")

    def test_set_name(self):
        """Test de setter voor naam."""
        drink = Drink("XX-0001", "Spa water", 0.5, 6, "13-10-2026")
        drink.set_name("Evian")
        self.assertEqual(drink.get_name(), "Evian")

        with self.assertRaises(TypeError):
            drink.set_name(123)

    def test_set_unit_price_per_liter(self):
        """Test de setter voor eenheidsprijs."""
        drink = Drink("XX-0001", "Spa water", 0.5, 6, "13-10-2026")
        drink.set_unit_price_per_liter(1.5)
        self.assertEqual(drink.get_unit_price_per_liter(), 1.5)

        with self.assertRaises(ValueError):
            drink.set_unit_price_per_liter(-1.0)

    def test_set_quantity(self):
        """Test de setter voor hoeveelheid."""
        drink = Drink("XX-0001", "Spa water", 0.5, 6, "13-10-2026")
        drink.set_quantity(10)
        self.assertEqual(drink.get_quantity(), 10)

        with self.assertRaises(ValueError):
            drink.set_quantity(-5)

    def test_add_quantity(self):
        """Test de add_quantity-methode."""
        drink = Drink("XX-0001", "Spa water", 0.5, 6, "13-10-2026")
        drink.add_quantity(4, "+")
        self.assertEqual(drink.get_quantity(), 10)

        drink.add_quantity(3, "-")
        self.assertEqual(drink.get_quantity(), 7)

        with self.assertRaises(ValueError):
            drink.add_quantity(10, "-")  # Negatief resultaat

        with self.assertRaises(ValueError):
            drink.add_quantity(5, "*")  # Ongeldige operator

    def test_str_representation(self):
        """Test de stringrepresentatie van het object."""
        drink = Drink("XX-0001", "Spa water", 0.5, 6, "13-10-2026")
        expected_output = (
            "Drink Information:\n"
            "  ID:               XX-0001\n"
            "  Name:             Spa water\n"
            "  Unit Price/L (€): 0.50\n"
            "  Quantity:         6\n"
            "  Expiration Date:  13-10-2026"
        )
        self.assertEqual(str(drink), expected_output)


if __name__ == "__main__":
    unittest.main()
