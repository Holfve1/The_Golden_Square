import pytest
from lib.presents import Present

def test_creating_a_contents_box():
    presents = Present()
    assert presents.contents == None

def test_wrap_the_contents():
    presents = Present()
    presents.wrap("Cake")
    with pytest.raises(Exception) as err:
        presents.wrap("Pie")
    error_message = str(err.value)
    assert error_message == ("A contents has already been wrapped.")

def if_contents_empty():
    presents = Present()
    with pytest.raises(Exception) as err:
        presents.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."



