import pytest
from unittest.mock import mock_open, patch
from read_file import read_file

@pytest.fixture
def mock_file():
    mock_data = "test data"
    with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
        yield mock_file, mock_data

def test_read_file(mock_file):
    mock_file_instance, expected_data = mock_file

    result = read_file("dummy.txt")

    assert result == expected_data  # ensure data is correctly read
    mock_file_instance.assert_called_once_with("dummy.txt", "r")  # file should be opened and closed