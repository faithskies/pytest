I configured all of the tests to be automatically run by GitHub Actions : https://github.com/faithskies/pytest/actions


src/basic_tests has some very basic tests for reference. Concepts covered: 
- basic asserts- Example assert user_manager.get_user("john_doe") == "john@example.com"
- validate return errors - Example pytest.raises(ValueError): user_manager.add_user("john_doe", "another@example.com")
- @pytest.fixture - allows for fresh instances for each test. yield if you want to define setup and teardown. 
- @pytest.mark.parametrize for when you have multiple values that need to be checked for test cases
