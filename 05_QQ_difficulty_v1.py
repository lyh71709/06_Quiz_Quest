
import random

def int_check(question):
    while True:
        try:
            response = int(input(question))
            return response
        # Error message
        except ValueError:
            print("Please enter an integer\n")
            continue

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
        # Added a while loop to generate valid numbers wehn dividing
        while (num_one/num_two) != (num_one//num_two):
            num_one = random.randint(2, 50)
            num_two = random.randint(2, 50)
            continue
        answer = num_one / num_two

    # Prints the question

    print(answer)
    if answer == 69:
        print("Hehe nice")
    # If statement when the subtraction equation is not valid
    if operator == "-" and cancel == "cancel":
        response = int(input("{} {} {} = ".format(num_two, operator, num_one)))
    # Normal response for every equation and valid subtraction equations
    else:
        response = int(input("{} {} {} = ".format(num_one, operator, num_two)))
    # Checks if the response is correct or incorrect
    if response == answer:
        print("Correct")
    else:
        print("Incorrect")
    print()

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
    response = (input("[{} _ {}] What is the missing operator (</>/=)? ".format(num_one, num_two)))

    #  Checks if the response matches the answer/ correct or incorrect
    if response == answer:
        print("Correct")
    else:
        print("Incorrect")

# Main Code goes here
question_num = 0
low = 1
high = 20
# Set up lists to generate randomly from
que_options = ["basic_facts", "basic_facts", "inequation"]
operators = ["+", "-", "x", "/"]

# For loop to generate 5 questions
for item in range(0,5):

    print("Question {}\n".format(question_num + 1))
    que_type = random.choice(que_options)

    if que_type == "basic_facts":
        question = basic_facts_q(random.choice(operators), random.randint(low, high), random.randint(low, high))
    else:
        question = inequation_q(random.randint(low, high), random.randint(low, high))

    question_num += 1
    high += 10
