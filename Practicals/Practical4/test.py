import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(12, 3) == 15
    assert add(-10, 1) == -9
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(51, 30) == 81
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(0, 1) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)