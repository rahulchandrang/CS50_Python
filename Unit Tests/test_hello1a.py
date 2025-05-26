from hello1 import hello


def test_default():
    assert hello() == "hello, world" # HEre we used assert since we have return value in hello function


def test_argument():
    assert hello("David") == "hello, David"
