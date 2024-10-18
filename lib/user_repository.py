from lib.user import *

class UserRepository:
    
    def __init__(self, connection):
        self.connection = connection
        
    def all(self):
        rows = self.connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["email"])
            users.append(item)
        return users
    
    def find(self, user_id):
        rows = self.connection.execute('SELECT * from users WHERE id = %s', [user_id])
        row = rows [0]
        return User(row["id"], row["username"], row["email"])
    
    def create(self, user):
        self.connection.execute('INSERT INTO users (username, email) VALUES (%s, %s)', [
                                 user.username, user.email])
        return None
    
    def delete(self, user_id):
        self.connection.execute('DELETE FROM users WHERE Id = %s', [user_id])
        return None