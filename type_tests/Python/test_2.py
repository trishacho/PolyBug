import unittest

class TestSlugify(unittest.TestCase):

    def test_empty_string(self):
        # Test empty string input
        result = slugify("")
        self.assertEqual(result, "")

    def test_null_input(self):
        # Test None input
        result = slugify(None)
        self.assertEqual(result, "")

    def test_valid_string(self):
        # Test a valid string without any special characters
        result = slugify("validString123")
        self.assertEqual(result, "validString123")

    def test_string_with_invalid_chars(self):
        # Test a string with spaces and special characters
        result = slugify("invalid string!@#")
        self.assertEqual(result, "invalid_string___")

    def test_string_starting_with_digit(self):
        # Test a string starting with a digit
        result = slugify("123startWithDigit")
        self.assertEqual(result, "_123startWithDigit")

if __name__ == '__main__':
    unittest.main()