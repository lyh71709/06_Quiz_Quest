# Quiz Quest Component 1c - get user input for certain variables needed (Trialling)
# I used Mrs Gottschalk's string checker and altered the code a bit to make it work with the rest of my code

# String Checker Function
answer = ["yes", "no", "maybe"]

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

# For loop loops three times for testing purposes
for item in range(0,4):
    question = str_checker("Is the sky blue? ", answer, "Yes, No or Maybe").lower()

    # If statements to check if the question variable works as intended
    if question == "yes" or question == "y":
        print("Correct")
    elif question == "no" or question == "n":
        print("Incorrect")
    else:
        print("Pseudo-Correct")
    print()


