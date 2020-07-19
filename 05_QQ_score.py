# Quiz Quest Component 6 - Score Keeping

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
    answer = 0
    cancel = ""

    # Addition question
    if operator == "+":
        answer = num_one + num_two

    # Subtraction question
    elif operator == "-":
        # Ensures that the difference is a positive integer or 0
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
        que_outcome = "Correct"
        print(que_outcome + "\n")
    else:
        que_outcome = "Incorrect"
        print(que_outcome + " the correct answer was {}\n".format(answer))
    return que_outcome

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
        que_outcome = "Correct"
        print(que_outcome + "\n")
    else:
        que_outcome = "Incorrect"
        print(que_outcome + " the correct answer was {}\n".format(answer))
    return que_outcome


# Main Code goes here
question_num = 0
outcome = []
low = 1
high = 50
# Set up lists to generate randomly from
que_options = ["basic_facts", "basic_facts", "inequation"]
operators = ["+", "-", "x", "/"]

# For loop to generate 5 questions
# In the real game the number of questions will exceed 5 questions
for item in range(0,5):
    print("Question {}\n".format(question_num + 1))
    que_type = random.choice(que_options)

    if que_type == "basic_facts":
        question = basic_facts_q(random.choice(operators), random.randint(low, high), random.randint(low, high))
    else:
        question = inequation_q(random.randint(low, high), random.randint(low, high))

    # Adds 1 to question number after every question
    question_num += 1

    # Adds variables to lists so that they can be printed as stats
    outcome.append(question)
    correct_num = outcome.count("Correct")

# Overall Game Stats are done here
list_count = 1
print("Game Results")
print("You got {} / 5 correct\n".format(correct_num))

for thing in outcome:
    print("Question {}: {}".format(list_count, thing))
    list_count += 1
