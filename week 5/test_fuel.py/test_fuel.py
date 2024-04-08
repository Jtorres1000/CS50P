from fuel import convert, gauge
import pytest

def test_zero_division():

    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_value_error():

    with pytest.raises(ValueError):
        convert("10/5")

def test_correct_fraction():
    assert convert("1/2") == 50

def test_hundred():
    assert gauge(100) == "F"

def test_nine():
    assert gauge(99) == "F"

def test_correct_print():
    assert gauge(50) == "50%"
    
def test_one():
    assert gauge(1) == "E"
