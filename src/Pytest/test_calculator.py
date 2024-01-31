from calculator import add

def test_add():
    assert add(1, 2) == 3
    assert add(5, 5) == 10


# test_fixture_example.py

import pytest

@pytest.fixture
def some_data():
    return 42

def test_some_data(some_data):
    assert some_data == 42
