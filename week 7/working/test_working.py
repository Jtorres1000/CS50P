from working import convert

import pytest

def test_value():
     with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_return_value():
    assert convert('6 AM to 9 PM') == '06:00 to 21:00'
    assert convert('8:30 AM to 11:30 PM') == '08:30 to 23:30'
