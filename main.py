from user_interface import UserInterface
from user_repository import UserRepository
from secret_repository import SecretsRepository

def main():
    secretsRepository = SecretsRepository()
    userRepository = UserRepository()
    userInterface = UserInterface()


    userInterface.welcome()
    response = userInterface.prompt1()

    print(f"Users's response {response}")
    
if __name__ == "__main__":
    main()
