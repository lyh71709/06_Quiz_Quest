# Quiz Quest Component 3 - Generate basic fact questions from the random numbers generated

import random

# Function for Basic facts questions goes here
def basicfacts_q(operator,one,two):

    # Addition question
    if operator == "+":
        answer = one + two

    # Subtraction question
    elif operator == "-":
        answer = one - two

    # Multiplication question
    elif operator == "x":
        answer = one * two

    # Divide question
    else:
        answer = one / two

    # Prints the question
    print(answer)
    response = int(input("{} {} {} = ".format(one,operator,two)))

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