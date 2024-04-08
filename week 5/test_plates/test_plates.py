from plates import is_valid

def test_length():
    assert is_valid("A") == False

def test_placement():
    assert is_valid("AA1A") == False

def test_alpha():
    assert is_valid("AA.2") == False

def test_start():
    assert is_valid("12") == False

def test_zero():
    assert is_valid("AA01") == False


