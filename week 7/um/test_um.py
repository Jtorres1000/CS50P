from um import count

def test_return_value():
    assert count("um um um") == 3
    assert count("um?") == 1

def test_return_incorrect_value():
    assert count("yummy") == 0
    assert count("uum") == 0
    
def test_case():
    assert count("Um, uM, UM") == 3
