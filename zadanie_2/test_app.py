import unittest
from app import (
    is_valid_email,
    calculate_area,
    filter_even,
    convert_date_format,
    is_palindrome
)

class TestAppFunctions(unittest.TestCase):
    """Testy jednostkowe dla funkcji w app.py"""

    def setUp(self):
        """Przygotowanie danych testowych."""
        self.valid_email = "test@example.com"
        self.invalid_email_no_at = "testexample.com"
        self.invalid_email_no_domain = "test@"

        self.circle_radius = 1
        self.rectangle_dims = (2, 3)
        self.triangle_dims = (3, 4)
        self.invalid_shape = "hexagon"

        self.valid_date = "2025-04-27"
        self.invalid_date = "27-04-2025"

        self.even_list = [1, 2, 3, 4, 5, 6]
        self.odd_list = [1, 3, 5]
        self.empty_list = []

        self.palindrome_true = "kajak"
        self.palindrome_false = "python"
        self.palindrome_mixed = "Kajak"

    # Testy dla is_valid_email
    def test_valid_email(self):
        """Sprawdza poprawny adres e-mail."""
        self.assertTrue(is_valid_email(self.valid_email))

    def test_invalid_email_no_at(self):
        """Sprawdza adres e-mail bez znaku @."""
        self.assertFalse(is_valid_email(self.invalid_email_no_at))

    def test_invalid_email_no_domain(self):
        """Sprawdza adres e-mail bez domeny."""
        self.assertFalse(is_valid_email(self.invalid_email_no_domain))

    # Testy dla calculate_area
    def test_calculate_area_circle(self):
        """Sprawdza obliczanie pola koła."""
        self.assertAlmostEqual(calculate_area("circle", self.circle_radius), 3.14159, places=5)

    def test_calculate_area_rectangle(self):
        """Sprawdza obliczanie pola prostokąta."""
        self.assertEqual(calculate_area("rectangle", *self.rectangle_dims), 6)

    def test_calculate_area_triangle(self):
        """Sprawdza obliczanie pola trójkąta."""
        self.assertEqual(calculate_area("triangle", *self.triangle_dims), 6)

    def test_calculate_area_invalid_shape(self):
        """Sprawdza reakcję na nieobsługiwany kształt."""
        with self.assertRaises(ValueError):
            calculate_area(self.invalid_shape, 3, 4)

    # Testy dla filter_even
    def test_filter_even_numbers(self):
        """Sprawdza filtrowanie liczb parzystych."""
        self.assertEqual(filter_even(self.even_list), [2, 4, 6])

    def test_filter_even_empty_list(self):
        """Sprawdza działanie przy pustej liście."""
        self.assertEqual(filter_even(self.empty_list), [])

    def test_filter_even_no_even_numbers(self):
        """Sprawdza działanie przy braku liczb parzystych."""
        self.assertEqual(filter_even(self.odd_list), [])

    # Testy dla convert_date_format
    def test_convert_date_format_valid(self):
        """Sprawdza poprawną konwersję daty."""
        self.assertEqual(convert_date_format(self.valid_date), "27/04/2025")

    def test_convert_date_format_invalid(self):
        """Sprawdza błędną konwersję daty."""
        with self.assertRaises(ValueError):
            convert_date_format(self.invalid_date)

    # Testy dla is_palindrome
    def test_is_palindrome_true(self):
        """Sprawdza poprawne rozpoznanie palindromu."""
        self.assertTrue(is_palindrome(self.palindrome_true))

    def test_is_palindrome_false(self):
        """Sprawdza rozpoznanie nie-palindromu."""
        self.assertFalse(is_palindrome(self.palindrome_false))

    def test_is_palindrome_case_insensitive(self):
        """Sprawdza palindrom niezależnie od wielkości liter."""
        self.assertTrue(is_palindrome(self.palindrome_mixed))

if __name__ == "__main__":
    unittest.main()
