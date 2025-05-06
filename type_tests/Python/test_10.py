import unittest
from io import StringIO
import sys
from notebook import display_info, User

# Unit test class
class TestCalculation(unittest.TestCase):

    def test_missing_value(self):
        variables = [
            User("name1", 5, {"nb": 5},{"team": 5}),
            User("name1", 6, {}, {"team": "Liverpool"}),
            User("name1", 7, {"nb": "Name"},{"team": "Liverpool"})
        ]
        display_info(variables)

    def test_standard(self):
        variables = [
            User("name1", 5, {"nb": 5},{"team": 5}),
            User("name1", 6, {"nb": 5}, {"team": "Liverpool"}),
            User("name1", 7, {"nb": "Name"},{"team": "Liverpool"})
        ]
        display_info(variables)

if __name__ == '__main__':
    unittest.main()
