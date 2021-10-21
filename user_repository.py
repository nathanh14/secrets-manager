class UserRepository:
    """Store and Get users"""
    def __init__(self) -> None:
        self.users = {}

    def store(self, key, value) -> None:
        self.users[key] = value

    def get(self, key):
        return self.users[key]