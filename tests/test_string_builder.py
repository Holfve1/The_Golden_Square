from lib.string_builder import *

def test_building_a_string():
    word = StringBuilder()
    word.add("Word")
    word.size()
    result = word.output()
    assert result == "Word"