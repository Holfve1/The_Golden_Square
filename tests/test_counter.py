from lib.counter import *

def test_counting_the_counter():
    number = Counter()
    number.add(7)
    result = number.report()
    assert result == f"Counted to 7 so far."