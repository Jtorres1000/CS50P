from numb3rs import validate
def test_value():
    assert validate("255.255.255.255") == True
    assert validate("144.1.0.21") == True
    assert validate("0.0.0.0") == True
    assert validate("3000.1.255.255") == False
    assert validate("1.25555.255.255") == False
def test_type():
    assert validate("cat") == False

def test_byte():
    assert validate("1.555.555.555") == False

