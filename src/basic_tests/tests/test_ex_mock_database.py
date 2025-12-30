# mocks the function of the database so we can test the code without actually needing to set up the database
from ex_mock_database import save_user

def test_save_user(mocker):
    mock_conn = mocker.patch("sqlite3.connect") 
    mock_cursor = mock_conn.return_value.cursor.return_value 

    save_user("Alice", 30) # calls that save_user function, and uses the mocks the connection and cursor 
              
    mock_conn.assert_called_once_with("users.db")  #tests that the database was called 
    #verifies that the correct values were asserted
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users (name, age) VALUES (?,?)", ("Alice", 30)
    )