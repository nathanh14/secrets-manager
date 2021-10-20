class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def __str__(self):
        return f'Users username is {self.username} and password is {self.password}'

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

class UserRepository:
    """Store and Get users"""
    def __init__(self) -> None:
        self.users = {}

    def store(self, key, value) -> None:
        self.users[key] = value

    def get(self, key):
        return self.users[key]

class UserInterface:
    """Handle inputs and present prompts"""

    def welcome(self):
        print("")
        print("Welcome to secrets manager")
        print("")

    def prompt1(self):
        print("")
        print("Login as an existing user   (L)")
        print("Create an account and login (C)")
        print("Exit                        (E)")
        print("")

        user_input = input("enter letter shown\n\n")
        return user_input

    def validate_input(self):
        """private function"""
        pass


def main():
    secretsRepository = SecretsRepository()
    userRepository = UserRepository()
    userInterface = UserInterface()


    userInterface.welcome()
    response = userInterface.prompt1()

    print(f"Users's response {response}")
    


if __name__ == "__main__":
    main()
