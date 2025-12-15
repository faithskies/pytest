#Examples of some basic assertion tests. Also includes with pytest.raises(ValueError, match=

from main import get_weather, add, divide
import pytest

def test_get_weather():
    assert get_weather(50) == "cold",  "If its 50 degrees then its cold"
    assert get_weather(85) == "hot", "If its 85 degrees then its hot"
    # if the test is true then it passes. If it does not match, then the test fails


def test_add(): 
    assert add(2, 5) == 7, "2 + 5 should be 7"
    assert add(-2, 2) == 0, "-2 plus 2 should be 0"
    assert add(0, 0) == 0, "0 plus 0 should be zero"

def test_divide():
    #makes sure it raises the error
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)