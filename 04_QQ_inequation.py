# Quiz Quest Component 4 - Inequation Questions

import random


# New in-equation function for in-equation questions
def inequation_q(one, two):

    # Code here determines the answer
    if one < two:
        answer = "<"
    elif one > two:
        answer = ">"
    else:
        answer = "="

    print(answer)
    # I haven't put in an intchecker
    response = (input("[{} _ {}] What is the missing operator (</>/=)? ".format(one, two)))

    #  Checks if the response matches the answer/ correct or incorrect
    if response == answer:
        print("Correct")
    else:
        print("Incorrect")

# Low and High is set to default
low = 1
high = 50

# Question uses the function and the one and two variables are randomly generated numbers
question = inequation_q(random.randint(low, high), random.randint(low, high))