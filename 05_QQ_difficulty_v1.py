# Quiz Quest Component 5 - Difficulty

# Fuse all previous components to make a work-in-progress while adding the slight modification
#  of adding the 10 to the high variable after every question to make the game gradually more difficult

import random


# String Checker goes here
def str_check(question, to_check, error):
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

# Int-checker function goes here
def int_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        # Error message
        except ValueError:
            print("Please enter an integer\n")
            continue


# Basic facts function goes here
def basic_facts_q(operator, num_one, num_two):

    # Addition question
    if operator == "+":
        answer = num_one + num_two

    # Subtraction question
    elif operator == "-":
        # Ensures that the difference is a postive integer or 0
        answer = num_one - num_two
        cancel = "0"
        # If the first answer is a negative integer it will switch one and two around to make the answer positive
        if answer < 0:
            cancel = ""
            answer = num_two - num_one

    # Multiplication question
    elif operator == "x":
        # Ensures that the numbers being multiplied have a product less that 144
        num_one = random.randint(0, 12)
        num_two = random.randint(0, 12)
        answer = num_one * num_two

    # Divide question
    else:
        # Added a while loop to generate valid numbers wehn dividing
        while (num_one/num_two) != (num_one//num_two):
            num_one = random.randint(low, high)
            num_two = random.randint(low, high)
            continue
        answer = num_one / num_two

    # Prints the question and answer for testing purposes
    print(answer)
    if answer == 69:
        print("Hehe nice")
    # If statement when the subtraction equation is not valid
    if operator == "-" and cancel == "":
        response = int_check("{} {} {} = ".format(num_two, operator, num_one))
    # Normal response for every equation and valid subtraction equations
    else:
        response = int_check("{} {} {} = ".format(num_one, operator, num_two))

    # Checks if the response is correct or incorrect
    if response == answer:
        print("Correct")
    else:
        print("Incorrect")

    print()
    return response

# In-equation Function
def inequation_q(num_one, num_two):

    # Code here determines the answer
    if num_one < num_two:
        answer = "<"
    elif num_one > num_two:
        answer = ">"
    else:
        answer = "="

    print(answer)
    # I haven't put in an intchecker
    inequations = ["<", ">", "="]
    response = str_check("[{} _ {}] What is the missing operator (</>/=)? ".format(num_one, num_two), inequations, "<, > or =")

    # Checks if the response is correct or incorrect
    if response == answer:
        print("Correct")
    else:
        print("Incorrect")

    print()
    return response


# Main Code goes here
question_num = 0
low = 1
high = 20
# Set up lists to generate randomly from
que_options = ["basic_facts", "basic_facts", "inequation"]
operators = ["+", "-", "x", "/"]

# For loop to generate 5 questions
# In the real game the number of questions will exceed 5 questions
for item in range(0,10):

    print("High = {}    Low = {}    Question No. = {}\n".format(high, low, question_num))

    print("Question {}\n".format(question_num + 1))
    que_type = random.choice(que_options)

    if que_type == "basic_facts":
        question = basic_facts_q(random.choice(operators), random.randint(low, high), random.randint(low, high))
    else:
        question = inequation_q(random.randint(low, high), random.randint(low, high))

    # Adds 1 to question number after every question and adds 8 to high to ensure question 10 has a high of 100
    question_num += 1
    high += 8
