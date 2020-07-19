# Quiz Quest Compnum_onent 3 - Generate basic fact questions from the random numbers generated

# v2 - Ensures that the difficulty of the quiz is not too difficult and ensures that all questions are suitable to be
#      answered without a calculator.
#      e.g. division equals a whole number, subtraction doesn't go negative and multiplication answers don't surpass 144.

import random


# Function for Basic facts questions goes here
def basic_facts_q(operator, num_one, num_two):
    answer = 0
    cancel = ""

    # Addition question
    if operator == "+":
        answer = num_one + num_two

    # Subtraction question
    elif operator == "-":
        # Ensures that the difference is a postive integer or 0
        answer = num_one - num_two
        cancel = "0"
        # If the first answer is a negative integer it will switch num_one and num_two around to make the answer positive
        if answer < 0:
            cancel = "cancel"
            answer = num_two - num_one

    # Multiplication question
    elif operator == "x":
        # Ensures that the numbers being multiplied have a product less that 144
        num_one = random.randint(0, 12)
        num_two = random.randint(0, 12)
        answer = num_one * num_two

    # Divide question
    else:
        num_one = random.randint(0, 12)
        num_two = random.randint(0, 12)
        product = num_one * num_two
        answer = num_two

    # Prints the question
    # If statement when the subtraction equation is not valid
    if operator == "-" and cancel == "cancel":
        response = int(input("{} {} {} = ".format(num_two, operator, num_one)))
    elif operator == "/":
        response = int(input("{} {} {} = ".format(product, operator, num_one)))
    # Normal response for every equation and valid subtraction equations
    else:
        response = int(input("{} {} {} = ".format(num_one, operator, num_two)))
    # Checks if the response is correct or incorrect
    if response == answer:
        print("Correct")
    else:
        print("Incorrect")
    print()


operators = ["+", "-", "x", "/"]
# Low/High set to default for testing purposes
low = 1
high = 50

# question uses the basicfacts_q function to make a random question
# Chooses randomly an operator and the num_two numbers that make up the equation
question = basic_facts_q("/", random.randint(low, high), random.randint(low ,high))
