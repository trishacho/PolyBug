import unittest
from io import StringIO
import sys
from notebook import display_info, User

# Unit test class
class TestCalculation(unittest.TestCase):
    
    def test_dev(self):
        variables = [
            User("name1", 5, {"nb":1},{"team":"Arsenal"}) # Should not break since 5 should be cast to string
        ]
        display_info(variables)


if __name__ == '__main__':
    unittest.main()
