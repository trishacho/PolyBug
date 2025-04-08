import unittest
from io import StringIO
import sys

# Assuming this is the code with the bug
class Calculation:
    def __init__(self, value):
        self.value = value

    def display_result(self):
        print("Result: " + str(self.value))  # Cast value to string here

# Unit test class
class TestCalculation(unittest.TestCase):

    def test_display_result(self):
        # Create a Calculation object with an integer value
        calc = Calculation(10)
        
        # Redirect stdout to capture the print statement
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the method
        calc.display_result()
        
        # Check if the output is correct (it should be "Result: 10")
        self.assertEqual(captured_output.getvalue(), "Result: 10\n")
        
        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_display_result_with_string(self):
        # Create a Calculation object with a string value
        calc = Calculation("Test")
        
        # Redirect stdout to capture the print statement
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the method
        calc.display_result()
        
        # Check if the output is correct (it should be "Result: Test")
        self.assertEqual(captured_output.getvalue(), "Result: Test\n")
        
        # Reset stdout
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
