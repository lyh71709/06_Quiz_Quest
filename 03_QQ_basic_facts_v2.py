# Quiz Quest Component 3 - Generate basic fact questions from the random numbers generated
# v2 - Ensures that the difficulty of the quiz is not too difficult for
#      easy difficulty and ensures that all questions are suitable to be answered without a calculator
#      e.g. division equals a whole number, subtraction doesn't go negative and multiplication answers don't surpass 144.

import random


# Function for Basic facts questions goes here
def basic_facts_q(operator, one, two):

    # Addition question
    if operator == "+":
        answer = one + two

    # Subtraction question
    elif operator == "-":
        # Ensures that the difference is a postive integer or 0
        answer = one - two
        cancel = "0"
        # If the first answer is a negative integer it will switch one and two around to make the answer positive
        if answer < 0:
            cancel = "cancel"
            answer = two - one

    # Multiplication question
    elif operator == "x":
        # Ensures that the numbers being multiplied have a product less that 144
        one = random.randint(0, 12)
        two = random.randint(0, 12)
        answer = one * two

    # Divide question
    else:
        # Added a while loop to generate valid numbers wehn dividing
        while (one/two) != (one//two):
            one = random.randint(2, 50)
            two = random.randint(2, 50)
            continue
        answer = one / two

    # Prints the question

    print(answer)
    if answer == 69:
        print("Hehe nice")
    # If statement when the subtraction equation is not valid
    if operator == "-" and cancel == "cancel":
        response = int(input("{} {} {} = ".format(two, operator, one)))
    # Normal response for every equation and valid subtraction equations
    else:
        response = int(input("{} {} {} = ".format(one, operator, two)))
    # Checks if the response is correct or incorrect
    if response == answer:
        print("Correct")
    else:
        print("Incorrect")
    print()

operators = ["+", "-", "x", "/"]
# Low/High (Difficulty) set to easy for testing purposes
low = 1
high = 50

# Generates 10 questions to test randomness
for item in range(0, 4):
    # question uses the basicfacts_q function to make a random question
    # Chooses randomly an operator and the two numbers that make up the equation
    question = basic_facts_q(random.choice(operators), random.randint(low,high), random.randint(low,high))
