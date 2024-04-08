from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.cookies == 0
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.cookies == 1
    jar.deposit(10)
    assert jar.cookies == 11
    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(2)
    assert jar.cookies == 0
    with pytest.raises(ValueError):
        jar.withdraw(2)

