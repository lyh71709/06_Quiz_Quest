# Quiz Quest Component 1c - get user input for certain variables needed (Trialling)

# String Checker Function
dif_range = ["hard", "normal", "easy"]

# Mrs Gottschalk's string checker starts here (edited)
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
        print("Please enter either {}\n".format(error))
# Mrs Gottschalk's string checker ends here (edited)

# For loop for testing purposes
for item in range(0,2):
    difficulty = str_checker("Difficulty (Easy, Normal or Hard): ",dif_range, "Hard, Normal or Easy").lower()


