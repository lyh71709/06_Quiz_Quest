# Quiz Quest Compnum_onent 3 - Generate basic fact questions from the random numbers generated

import random

# Function for Basic facts questions goes here
def basicfacts_q(operator,num_one,num_two):

    # Addition question
    if operator == "+":
        answer = num_one + num_two

    # Subtraction question
    elif operator == "-":
        answer = num_one - num_two

    # Multiplication question
    elif operator == "x":
        answer = num_one * num_two

    # Divide question
    else:
        answer = num_one / num_two

    # Prints the question
    print(answer)
    response = int(input("{} {} {} = ".format(num_one,operator,num_two)))

    # Checks if the response is correct or incorrect
    if response == answer:
        print("Correct")
    else:
        print("Incorrect")
    print()

operators = ["+", "-", "x", "/"]
low = 1
high = 50

for item in range(0,10):
    question = basicfacts_q("-", random.randint(low,high), random.randint(low,high))
