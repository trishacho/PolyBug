
import unittest
from uuid import UUID
from typing import Any

class Tag:
    
    def __init__(
        self,
        id: UUID,
        user: int,
        title: str,
        picture: str,
        show_income: bool,
        show_outcome: bool,
        budget_income: bool,
        budget_outcome: bool,
        changed: int,
        color: int,
        static_id: int | None = None,
        icon: str | None = None,
        parent: UUID | None = None,
        required: bool | None = None
    ):
        self.id = id
        self.user = user
        self.title = title
        self.picture = picture
        self.show_income = show_income
        self.show_outcome = show_outcome
        self.budget_income = budget_income
        self.budget_outcome = budget_outcome
        self.changed = changed
        self.color = color
        self.static_id = static_id
        self.icon = icon
        self.parent = parent
        self.required = required

    @staticmethod
    def from_dict(obj: dict) -> 'Tag':
        #check_dict_type(obj)

        return Tag(
            id=UUID(obj.get("id")),
            user=from_int(obj.get("user")),
            title=from_str(obj.get("title")),
            picture=from_none(obj.get("picture")),
            show_income=from_bool(obj.get("showIncome")),
            show_outcome=from_bool(obj.get("showOutcome")),
            budget_income=from_bool(obj.get("budgetIncome")),
            budget_outcome=from_bool(obj.get("budgetOutcome")),
            changed=from_int(obj.get("changed")),
            color=from_union([from_none, from_int], obj.get("color")),
            static_id=from_union([from_none, lambda x: int(from_str(x))], obj.get("staticId")),
            icon=from_union([from_none, from_str], obj.get("icon")),
            parent=from_union([from_none, lambda x: UUID(x)], obj.get("parent")),
            required=from_union([from_bool, from_none], obj.get("required")),
        )

def from_none(value: Any) -> Any:
    if value is not None:
        raise TypeError(f"Expected None, got {type(value).__name__}")
    return value

def from_str(value):
    if type(value) is not str:
        raise TypeError("Wrong Type (from string)")
    return value

def from_bool(value):
    if type(value) is not bool:
        raise TypeError("Wrong Type (from bool)")
    return value

def from_int(value):
    if type(value) is not int:
        raise TypeError("Wrong Type (from int)")
    return value

def from_union(arr, value):
    return value

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
