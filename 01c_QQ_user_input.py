# Quiz Quest Component 1c - get user input for certain variables needed (Trialling)

# String Checker
dif_range = ["hard", "normal", "easy"]


def str_checker(question, to_check, error):
    valid = False
    while not valid:

        # Ask question
        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item
        print("Please enter either {}".format(error))

# Set all the vaiables when do
difficulty = str_checker("Difficulty (Easy, Normal or Hard): ",dif_range, "Hard, Normal or Easy").lower()

if difficulty == "easy" or difficulty == "e":
    high = 10
elif difficulty == "normal" or difficulty == "n":
    high = 50
elif difficulty == "hard" or difficulty == "h":
    high = 100

print(high)