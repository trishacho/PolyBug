import unittest
from unittest.mock import MagicMock
from process_retention_param import process_retention_param

class TestRetentionParam(unittest.TestCase):

    def test_retention_none(self):
        # Test case where args.retention is None
        args = MagicMock()
        args.retention = None
        
        # Mock the parser object
        parser_object = MagicMock()
        
        # Call the function (no error should occur)
        process_retention_param(args, parser_object)
        
        # Ensure that error was not called (since retention is None)
        parser_object.error.assert_not_called()

    def test_retention_empty(self):
        # Test case where args.retention is an empty list
        args = MagicMock()
        args.retention = []
        
        # Mock the parser object
        parser_object = MagicMock()
        
        # Call the function (no error should occur)
        process_retention_param(args, parser_object)
        
        # Ensure that error was not called
        parser_object.error.assert_not_called()

    def test_retention_valid(self):
        # Test case where args.retention has 2 values
        args = MagicMock()
        args.retention = [1, 2]
        
        # Mock the parser object
        parser_object = MagicMock()
        
        # Call the function (no error should occur)
        process_retention_param(args, parser_object)
        
        # Ensure that error was not called
        parser_object.error.assert_not_called()

    def test_retention_invalid(self):
        # Test case where args.retention has 3 values
        args = MagicMock()
        args.retention = [1, 2, 3]
        
        # Mock the parser object
        parser_object = MagicMock()
        
        # Call the function (error should occur)
        process_retention_param(args, parser_object)
        
        # Ensure that error was called with the correct message
        parser_object.error.assert_called_with('The "--retention or -r" parameter must have max two integers. Three or more arguments specified: [1, 2, 3]')

if __name__ == '__main__':
    unittest.main()
