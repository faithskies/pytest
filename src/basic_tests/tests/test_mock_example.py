# how to mock or create a fake version of that dependency 
# useful for if you want to fake an API response, so you can stay forcused on testing the frontend without needing to verify against backend

import pytest
from mock_example import get_weather

def test_get_weather(mocker):
    # mocks requests.get 
    mock_get = mocker.patch("mock_example.requests.get")

    # set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

    # call function 
    result = get_weather("Dubai")

    #assertions
    assert result == {"temperature": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai")

