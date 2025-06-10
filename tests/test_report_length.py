from lib.report_length import *

def test_report_length_john():

    result = report_length("John")

    assert result == f"This string was 4 characters long."

def test_report_length_daisy():

    result = report_length("Daisy")

    assert result == f"This string was 5 characters long."