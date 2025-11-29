
# displays at the start of the game
def welcome_message():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")


# displays difficulty option
# gets user input and validate it
def get_difficulty():
    print("Please select the difficulty level: ")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            return "easy"
        elif user_choice == "2":
            return "medium"
        elif user_choice == "3":
            return "hard"
        else:
            print("Invalid! Please enter 1,2 or 3")


def get_guess():
    while True:
        user_input = input("Enter your guess: ")
        try:
            guess = int(user_input)

            if guess > 0 and guess < 101:
                return guess
            else:
                print("Please input a number between 1-100 only.")
        except ValueError:
            print("Please enter a valid number!")


def correct_guess():
    print("Correct! You got it in {number of tries}! Would you like to play again?")

get_guess()



