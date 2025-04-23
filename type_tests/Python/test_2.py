import unittest
import string


class TestSlugify(unittest.TestCase):

    # Replace with actual slugify function
    def slugify(self, _string):
        valid_chars = frozenset("_{}{}".format(string.ascii_letters, string.digits))
        if not _string:
            return ""
        if _string[0].isdigit():
            _string = "_" + _string
        return "".join(c if c in valid_chars else "_" for c in _string)

    def test_empty_string(self):
        # Test empty string input
        result = self.slugify("")
        self.assertEqual(result, "")

    def test_null_input(self):
        # Test None input
        result = self.slugify(None)
        self.assertEqual(result, "")

    def test_valid_string(self):
        # Test a valid string without any special characters
        result = self.slugify("validString123")
        self.assertEqual(result, "validString123")

    def test_string_with_invalid_chars(self):
        # Test a string with spaces and special characters
        result = self.slugify("invalid string!@#")
        self.assertEqual(result, "invalid_string___")

    def test_string_starting_with_digit(self):
        # Test a string starting with a digit
        result = self.slugify("123startWithDigit")
        self.assertEqual(result, "_123startWithDigit")

if __name__ == '__main__':
    unittest.main()