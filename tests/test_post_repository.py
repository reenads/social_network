from lib.post_repository import *
from lib.post import *

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == [
Post(1,'Nineteen Eighty-Four', 'George Orwell', 23, 1),
Post(2, 'Mrs Dalloway', 'Virginia Woolf', 345, 1),
Post(3, 'Emma', 'Jane Austen', 45, 2),
Post(4, 'Dracula', 'Bram Stoker', 456, 3),
Post(5, 'The Age of Innocence', 'Edith Wharton', 100, 4)]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    posts = repository.find(2)
    assert posts == Post(2, 'Mrs Dalloway', 'Virginia Woolf', 345, 1)

                        
def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostRepository(db_connection)
    repository.create(Post(None, 'newtitle', 'Che Woolf', 345, 1))
    result = repository.all()
    assert result == [Post(1,'Nineteen Eighty-Four', 'George Orwell', 23, 1),
Post(2, 'Mrs Dalloway', 'Virginia Woolf', 345, 1),
Post(3, 'Emma', 'Jane Austen', 45, 2),
Post(4, 'Dracula', 'Bram Stoker', 456, 3),
Post(5, 'The Age of Innocence', 'Edith Wharton', 100, 4),
Post(6, 'newtitle', 'Che Woolf', 345, 1)]

                        
def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
Post(1,'Nineteen Eighty-Four', 'George Orwell', 23, 1),
Post(2, 'Mrs Dalloway', 'Virginia Woolf', 345, 1),
Post(4, 'Dracula', 'Bram Stoker', 456, 3),
Post(5, 'The Age of Innocence', 'Edith Wharton', 100, 4)]