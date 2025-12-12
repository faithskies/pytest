from main_basic_user_mgr import UserManager
import pytest

@pytest.fixture
def user_manager():
    """Creates a fresh instance of a UserManager before each test"""
    return UserManager()

#Tests

def test_add(): 
    assert UserManager.add(2, 5) == 7, "2 + 5 should be 7"

def test_add_user(user_manager): 
    assert user_manager.add_user("john_doe", "john@example.com") == True, "Add john_doe as a user"
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "another@example.com")

def test_add_multiple_users(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert user_manager.add_user("sue_smith", "sue@example.com") == True
    assert user_manager.get_user("john_doe") == "john@example.com"
    assert user_manager.get_user("sue_smith") == "sue@example.com"