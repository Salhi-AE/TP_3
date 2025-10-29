from src.string_calculator import add_numbers_from_string

def test_passing_empty_value_return_0():
    assert add_numbers_from_string("") == 0
def test_passing_0_return_0():
    assert add_numbers_from_string("0") == 0