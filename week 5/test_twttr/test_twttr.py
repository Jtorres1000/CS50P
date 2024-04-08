from twttr import shorten
#test for general vowels
def test_general():

    assert shorten("word") == "wrd"
    assert shorten("twitter") == "twttr"

#test for uppercase vowels
def test_uppercase():
    assert shorten("wOrD") == "wrD"
    assert shorten("TwIttEr") == "Twttr"

#test for ommiting numbers
def test_numbers():
    assert shorten("123lol") == "123ll"
    
#test for ommiting alphanumeric
def test_alpha():
    assert shorten("#!.twitter") == "#!.twttr"
