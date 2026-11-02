import unittest
from src.password_validator import validate_password

class TestPasswordValidator(unittest.TestCase):

    def test_valid_latin_password(self):
        self.assertTrue(validate_password("SecurePass1!"))

    def test_valid_cyrillic_password(self):
        self.assertTrue(validate_password("ПарольТест9#"))

    def test_boundary_length_7(self):
        self.assertFalse(validate_password("Pass1!a"))

    def test_boundary_length_8(self):
        self.assertTrue(validate_password("Pass1!ab"))

    def test_boundary_length_20(self):
        self.assertTrue(validate_password("A" * 16 + "a1!b"))

    def test_boundary_length_21(self):
        self.assertFalse(validate_password("A" * 17 + "a1!b"))

    def test_missing_upper(self):
        self.assertFalse(validate_password("securepass1!"))

    def test_missing_lower(self):
        self.assertFalse(validate_password("SECUREPASS1!"))

    def test_missing_digit(self):
        self.assertFalse(validate_password("SecurePassword!"))

    def test_missing_spec(self):
        self.assertFalse(validate_password("SecurePassword1"))

    def test_invalid_spec_character(self):
        self.assertFalse(validate_password("SecurePass1_"))

    def test_empty_string(self):
        self.assertFalse(validate_password(""))

    def test_value_error_with_spaces(self):
        with self.assertRaises(ValueError):
            validate_password("Pass 1234!")
        with self.assertRaises(ValueError):
            validate_password(" Pass1234!")
        with self.assertRaises(ValueError):
            validate_password("Pass1234! ")

    def test_type_error_invalid_types(self):
        with self.assertRaises(TypeError):
            validate_password(12345678)
        with self.assertRaises(TypeError):
            validate_password(None)
        with self.assertRaises(TypeError):
            validate_password(["P", "a", "s", "s", "1", "!"])


if __name__ == "__main__":
    unittest.main()
