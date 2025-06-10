from lib.check_codeword import *

def test_check_codeword_is_horse():

    result = check_codeword("horse")

    assert result == "Correct! Come in."

def test_check_codeword_start_h__end_e():

    result1 = check_codeword("hose")
    result2 = check_codeword("house")

    assert result1 == "Close, but nope."
    assert result2 == "Close, but nope."

def test_check_codeword():

    result = check_codeword("jimbo")

    assert result == "WRONG!"
