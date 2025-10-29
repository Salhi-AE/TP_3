import pytest
from src.string_calculator import add_numbers_from_string

@pytest.mark.parametrize('String,result_expected', [('',0),
                                                    ('0',0),
                                                    ('1',1),
                                                    ('2',2),
                                                    ('3',3),
                                                    ('4',4),
                                                    ('5',5),
                                                    ('6',6),
                                                    ('7',7),
                                                    ('8',8),
                                                    ('9',9),])
def test_string_return_result_expected(String, result_expected):
    actual_result = add_numbers_from_string(String)
    assert actual_result == result_expected