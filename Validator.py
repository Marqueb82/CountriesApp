class Validator:

    @staticmethod
    def inputNumber(message):
        while True:
            try:
                userInput = int(input(message))
                if userInput < 1 or userInput > 5:
                    print("\nInvalid menu selection.\n")
                    continue
            except ValueError:
                print("\nPlease enter a value from menu.\n")
                continue
            else:
                return userInput

    @staticmethod
    def inputPopulation(message):
        while True:
            try:
                userInput = int(input(message))
                if userInput < 100000:
                    print("\nMinimum accepted value is 100000 for population.\n")
                    continue
            except ValueError:
                print("\nPlease enter valid value for population.\n")
                continue
            else:
                return userInput

    @staticmethod
    def inputCountry(message):
        while True:
            userInput = input(message)
            if userInput != userInput.capitalize():
                print("\nFirst letter must be capitalized.\n")
                continue
            elif userInput.isdigit() or len(userInput) < 3:
                print("\nPlease enter value name for country.\n")
                continue
            else:
                return userInput
