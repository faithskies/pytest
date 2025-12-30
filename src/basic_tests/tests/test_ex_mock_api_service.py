import pytest
from ex_mock_api_service import UserService, APIClient

#mocking an entire class that is the API client

def test_get_username_with_mock(mocker):
        mock_api_client = mocker.Mock(spec=APIClient) # Create a mock API Client  

        #Mock the function get_user_data to return a fake user 
        mock_api_client.get_user_data.return_value = {"id": 1, "name": "Alice"}

        service = UserService(mock_api_client) # inject mock API Client 

        result = service.get_username(1) #Call method that depends on the previously mocked data 

        #Assertions
        assert result == "ALICE" # check if the processing was done correctly 
        mock_api_client.get_user_data.assert_called_once_with(1) #esnure correct API call 