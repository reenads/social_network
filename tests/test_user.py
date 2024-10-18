from lib.user import *

"""
user constructs with username and email
"""
def test_user_constructs():
    user = User(1, "Test USER", "Test EMAIL")
    assert user.id == 1
    assert user.username == "Test USER"
    assert user.email == "Test EMAIL"

# def __eq__(self, other):
#     return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an users
def test_result_formats():
    user = User(1, "Test USER", "Test EMAIL")
    assert str(user) == "User(1, Test USER, Test EMAIL)"

def test_objects_for_equality():
    user_1 = User(1, "Test USER", "Test EMAIL")
    user_2 = User(1, "Test USER", "Test EMAIL")
    assert user_1 == user_2