
import unittest
from uuid import UUID
from typing import Any
from tag import Tag

class TestTag(unittest.TestCase):

    def test_color_should_not_be_none(self):
        # Setup: Create an object dictionary that will be passed to from_dict
        obj = {
            "id": str(UUID(int=1234)),
            "user": 1,
            "title": "Test Title",
            "picture": None,
            "showIncome": True,
            "showOutcome": True,
            "budgetIncome": True,
            "budgetOutcome": True,
            "changed": 0,
            "color": None,
            "staticId": None,
            "icon": None,
            "parent": None,
            "required": None,
        }

        # Verify that when color is None, an error is raised (as color must be an int)
        with self.assertRaises(TypeError):
            res = Tag.from_dict(obj)

    def test_color_with_valid_int(self):
        # Setup: Create an object dictionary with a valid color value
        obj = {
            "id": str(UUID(int=1234)),
            "user": 1,
            "title": "Test Title",
            "picture": None,
            "showIncome": True,
            "showOutcome": True,
            "budgetIncome": True,
            "budgetOutcome": True,
            "changed": 0,
            "color": 123,  # Valid color (int)
            "staticId": None,
            "icon": None,
            "parent": None,
            "required": None,
        }

        # Create the Tag object from the dictionary
        tag = Tag.from_dict(obj)

        # Assert that the color is correctly set to the provided int value
        self.assertEqual(tag.color, 123)

if __name__ == '__main__':
    unittest.main()
