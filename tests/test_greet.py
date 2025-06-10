from lib.greet import *

def test_greet_hello_john():
    result = greet("John")

    assert result == "Hello, John!"

def test_greet_hello_sarah():
    result = greet("Sarah")

    assert result == "Hello, Sarah!"
