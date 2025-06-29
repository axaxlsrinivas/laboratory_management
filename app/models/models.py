class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def from_row(row):
        return User(row['id'], row['username'], row['password'])

class Item:
    def __init__(self, id, name, description, owner_id):
        self.id = id
        self.name = name
        self.description = description
        self.owner_id = owner_id

    @staticmethod
    def from_row(row):
        return Item(row['id'], row['name'], row['description'], row['owner_id'])
