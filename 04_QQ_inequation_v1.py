# Quiz Quest Component 4 - Inequation Questions

import random

# The same function as in basic facts but I will get rid of the other basic facts for this component
# ToF and basic facts questions will go in the same function
def missing_op_q(operator, one, two):

    if one < two:
        answer = "<"
    elif one > two:
        answer = ">"
    else:
        answer = "="

    print(answer)
    response = (input("[{} _ {}] What is the missing operator (</>/=)? ".format(one, two)))

    if response == answer:
        print("Correct")
    else:
        print("Incorrect")
low = 1
high = 50

operators = ["<", ">", "="]
question = missing_op_q(random.choice(operators), random.randint(low, high), random.randint(low, high))