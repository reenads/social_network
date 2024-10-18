from lib.user_repository import *
from lib.user import *

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [User(1,'reenads', 'george.orwell@gmail.com'),
User(2, 'sallyj', 'virginia.woolf@gmail.com'),
User(3, 'Emma', 'jane.asten@gmail.com'),
User(4, 'Dracula', 'bram.stoker@gmail.com'),
User(5, 'pqwer', 'edith.wharton@gmail.com')]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    users = repository.find(2)
    assert users == User(2, 'sallyj', 'virginia.woolf@gmail.com')

                        
def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection)
    repository.create(User(None, 'Chad', 'edithton@gmail.com'))
    result = repository.all()
    assert result == [User(1,'reenads', 'george.orwell@gmail.com'),
User(2, 'sallyj', 'virginia.woolf@gmail.com'),
User(3, 'Emma', 'jane.asten@gmail.com'),
User(4, 'Dracula', 'bram.stoker@gmail.com'),
User(5, 'pqwer', 'edith.wharton@gmail.com'),
User(6, 'Chad', 'edithton@gmail.com')
]

                        
def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [User(1,'reenads', 'george.orwell@gmail.com'),
User(2, 'sallyj', 'virginia.woolf@gmail.com'),
User(4, 'Dracula', 'bram.stoker@gmail.com'),
User(5, 'pqwer', 'edith.wharton@gmail.com')]