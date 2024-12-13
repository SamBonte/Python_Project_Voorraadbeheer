import unittest
from Snack import Snack

class TestSnack(unittest.TestCase):
    """Unittest klasse voor de Snack-klasse."""

    def test_valid_snack_creation(self):
        """Test het succesvol aanmaken van een Snack-object."""
        snack = Snack("SN-0001", "Twix", 1.25, 20, "15-12-2025")
        self.assertEqual(snack.get_unique_id(), "SN-0001")
        self.assertEqual(snack.get_name(), "Twix")
        self.assertEqual(snack.get_unit_price_per_piece(), 1.25)
        self.assertEqual(snack.get_quantity(), 20)
        self.assertEqual(snack.get_expiration_date(), "15-12-2025")

    def test_invalid_unique_id(self):
        """Test ongeldige unieke ID."""
        with self.assertRaises(ValueError):
            Snack("SN001", "Twix", 1.25, 20, "15-12-2025")  # Verkeerd formaat

    def test_invalid_name(self):
        """Test ongeldige naam."""
        with self.assertRaises(TypeError):
            Snack("SN-0001", 123, 1.25, 20, "15-12-2025")  # Naam moet string zijn

    def test_invalid_unit_price(self):
        """Test ongeldige eenheidsprijs."""
        with self.assertRaises(ValueError):
            Snack("SN-0001", "Twix", -1.25, 20, "15-12-2025")  # Negatieve prijs

    def test_invalid_quantity(self):
        """Test ongeldige hoeveelheid."""
        with self.assertRaises(ValueError):
            Snack("SN-0001", "Twix", 1.25, -5, "15-12-2025")  # Negatieve hoeveelheid

    def test_invalid_expiration_date(self):
        """Test ongeldige vervaldatum."""
        with self.assertRaises(ValueError):
            Snack("SN-0001", "Twix", 1.25, 20, "15/12/2025")  # Verkeerd datumformaat

    def test_set_name(self):
        """Test de set_name methode."""
        snack = Snack("SN-0001", "Twix", 1.25, 20, "15-12-2025")
        snack.set_name("Mars")
        self.assertEqual(snack.get_name(), "Mars")
        with self.assertRaises(TypeError):
            snack.set_name(123)  # Ongeldig datatype

    def test_set_unit_price_per_piece(self):
        """Test de set_unit_price methode."""
        snack = Snack("SN-0001", "Twix", 1.25, 20, "15-12-2025")
        snack.set_unit_price_per_piece(2.00)
        self.assertEqual(snack.get_unit_price_per_piece(), 2.00)
        with self.assertRaises(ValueError):
            snack.set_unit_price_per_piece(-2.00)  # Negatieve prijs

    def test_set_quantity(self):
        """Test de set_quantity methode."""
        snack = Snack("SN-0001", "Twix", 1.25, 20, "15-12-2025")
        snack.set_quantity(30)
        self.assertEqual(snack.get_quantity(), 30)
        with self.assertRaises(ValueError):
            snack.set_quantity(-10)  # Negatieve hoeveelheid

    def test_add_quantity(self):
        """Test de add_quantity methode."""
        snack = Snack("SN-0001", "Twix", 1.25, 20, "15-12-2025")
        snack.add_quantity(10, "+")
        self.assertEqual(snack.get_quantity(), 30)  # Toevoegen
        snack.add_quantity(5, "-")
        self.assertEqual(snack.get_quantity(), 25)  # Aftrekken
        with self.assertRaises(ValueError):
            snack.add_quantity(50, "-")  # Resulterende hoeveelheid mag niet negatief zijn

    def test_str_representation(self):
        """Test de stringrepresentatie van een Snack-object."""
        snack = Snack("SN-0001", "Twix", 1.25, 20, "15-12-2025")
        expected = (
            "Snack Information:\n"
            "  ID:               SN-0001\n"
            "  Name:             Twix\n"
            "  Unit Price (€):   1.25\n"
            "  Quantity:         20\n"
            "  Expiration Date:  15-12-2025"
        )
        self.assertEqual(str(snack), expected)

if __name__ == "__main__":
    unittest.main()
