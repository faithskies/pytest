# example of if you have mutliple parameters, that you would like to test without having to assert each one individually

import pytest
from example_multiple_parameters import is_prime


@pytest.mark.parametrize("num, expected", [
    # setting up mutliple paramaters to be checked. If prime it returns False 
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (19, True),
    (25, False),                                 
])

def test_check_prime(num, expected):
    assert is_prime(num) == expected 