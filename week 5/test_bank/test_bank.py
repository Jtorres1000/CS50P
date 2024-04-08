from bank import value

#test uppercase values
def test_uppercase():

    assert value("HELLO") == 0

#test for 20 return
def test_twenty():
    assert value("hi!") == 20

#test for 100 return
def test_hundred():
    assert value("What's up?") == 100
