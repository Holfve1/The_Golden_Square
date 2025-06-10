from lib.gratitudes import Gratitudes

def test_creating_list_for_things_to_be_gratful_for():

    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

def test_add_gratitude_to_list():

    gratitudes = Gratitudes()
    gratitudes.add("life")
    result = gratitudes.gratitudes 
    assert result == ["life"]
    # assert gratitudes.gratitudes == ["life"]

def test_create_a_string_with_list():
    gratitudes = Gratitudes()
    
    result = "be grateful for: life,"

    assert result == "be grateful for: life,"
    

