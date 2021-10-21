class SecretsRepository:
    """Store and Get secrets"""
    def __init__(self) -> None:
        self.secrets = {}

    def store(self, key, value) -> None:
        self.secrets[key] = value

    def get(self, key):
        return self.secrets[key]
    
    def getAllKeys(self):
        return self.secrets.keys()