# Example with Fixcture with a tear down operation 'yield'

import pytest
from example_db import Database

@pytest.fixture 
def db():
    
    database = Database() # Provides a fresh instance of the Database class and cleans up after the test 
    
    #The yield keyword in pytest is used within fixtures to define both setup and teardown logic within a single function. 
    # It splits the fixture's execution: the code before yield runs as setup, and the code after yield runs as cleanup once the test (or scope) finishes
    yield database  
    
    database.data.clear()  #cleanup step (not needed for in-memory but useful for a real database)

def test_add_user(db):
    db.add_user(1, "Bob")
    assert db.get_user(1) == "Bob"

def test_add_duplicate_user(db):
    db.add_user(1, "Bob")
    assert db.get_user(1) == "Bob"
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "Sarah")  , "User 1 already exists "

def test_delete_user(db):
    db.add_user(1, "Bob")
    db.delete_user(1) , "User succesfully deleted"
    assert db.get_user(1) == None