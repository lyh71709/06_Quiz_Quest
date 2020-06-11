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
        cancel = "0"
        if answer < 0:
            cancel = "cancel"
            answer = two - one

    # Multiplication question
    elif operator == "x":
        one = random.randint(0,12)
        two = random.randint(0,12)
        answer = one * two

    # Divide question
    else:
        valid = False
        while not valid:
            if (one/two) != (one//two):
                one = random.randint(20,50)
                two = random.randint(0,50)
                continue
            else:
                answer = one / two
                valid = True

    # Prints the question
    print(answer)
    if operator == "-" and cancel == "cancel":
        response = int(input("{} {} {} = ".format(two, operator, one)))
    else:
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

