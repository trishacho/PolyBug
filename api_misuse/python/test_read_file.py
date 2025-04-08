import pytest
from io import StringIO
from read_file import read_file_buggy, read_file_fixed

@pytest.fixture
def test_read_file_buggy():
    fake_file = StringIO("Hello, world!")
    data_buggy = read_file_buggy(fake_file)
    try:
        fake_file.read()
        file_closed_buggy = False
    except ValueError:
        file_closed_buggy = True
    assert not file_closed_buggy, "Buggy function incorrectly closed the file!"
    assert data_buggy == "Hello, world!"

@pytest.fixture
def test_read_file_fixed():
    fake_file = StringIO("Hello, world!")
    data_fixed = read_file_fixed(fake_file)
    try:
        fake_file.read()
        file_closed_fixed = False
    except ValueError:
        file_closed_fixed = True
    assert file_closed_fixed, "Fixed function failed to close the file!"
    assert data_fixed == "Hello, world!"