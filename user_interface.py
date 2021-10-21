class UserInterface:
    """Handle inputs and present prompts"""

    def welcome(self) -> None:
        print("")
        print("Welcome to secrets manager")
        print("")

    def prompt1(self):
        input_options = ["L", "C", "E"]
        print("")
        print("Login as an existing user   (L)")
        print("Create an account and login (C)")
        print("Exit                        (E)")
        print("")

        user_input = input("Select an option by typing the letter in brackets\n\n")
        is_valid_input = self.__validate_input(user_input, input_options)

        if (is_valid_input):
            print("Valid option selected")
        else:
            print("Invalid option selected")
            self.prompt1()
        return user_input

    def __validate_input(self, user_input: str, input_options: list) -> bool:
        """private function"""
        if user_input in input_options:
            return True
        return False