import pytest
from unittest.mock import mock_open, patch

def read_file(file_path):
    file = open(file_path, 'r')
    data = file.read()
    return data

def test_read_file():
    mock_data = "test data"

    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
        result = read_file("dummy.txt")

    assert result == mock_data  # Ensure data is correctly read
    mock_file.assert_called_once_with("dummy.txt", "r")  # File should be opened and closed

test_read_file()