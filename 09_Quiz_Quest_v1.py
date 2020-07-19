# Quiz Quest - Final Game
# v1 - Before usability test
import random


# Make a function for statement generation
def qq_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

    return statement


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
    product = 0
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
        response = int_check("{} {} {} = ".format(num_two, operator, num_one))
    elif operator == "/":
        response = int_check("{} {} {} = ".format(product, operator, num_one))
    # Normal response for every equation and valid subtraction equations
    else:
        response = int_check("{} {} {} = ".format(num_one, operator, num_two))

    # Checks if the response is correct or incorrect
    if response == answer:
        que_outcome = "Correct"
        correct = qq_statement("✔✔✔   You got it!   ✔✔✔   ", "-")
    else:
        que_outcome = "Incorrect"
        incorrect = qq_statement("❌❌❌   You got it wrong, the correct answer was {}   ❌❌❌     ".format(answer), "-")
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

    # I haven't put in an int checker
    inequations = ["<", ">", "="]
    response = str_check("[{} _ {}] What is the missing operator (</>/=)? ".format(num_one, num_two), inequations, "<, > or =")

    # Checks if the response is correct or incorrect
    if response == answer:
        que_outcome = "Correct"
        correct = qq_statement("✔✔✔   You got it!   ✔✔✔   ", "-")
    else:
        que_outcome = "Incorrect"
        incorrect = qq_statement("❌❌❌   You got it wrong, the correct answer was {}   ❌❌❌     ".format(answer), "-")
    return que_outcome


# Main Code goes here

# Introduction goes here
print("Welcome to Quiz Quest!\n")
print("This is a maths game where you answer basic facts and in-equation questions. "
      "It is very basic and easy, first choose which gamemode you want. Chosen Play is where the\n"
      "game asks you how many questions you want to do and will stop the game once you have finished\n"
      "answering your chosen amount of questions. Continuous Play is where the game will loop forever\n"
      "until whenever you wish to stop, after each question the game will ask if you want to stop playing\n"
      "after every question.\n"
      "Alright so have fun! and let the game begin!")
print()


# Asks for the gamemode
gamemodes = ["1", "2"]
how_many_que = 0
print("1 for Chosen Play (Choosing a set number of questions) or 2 for Continuous Play")
game_mode = str_check("What gamemode do you want? (1 or 2): ", gamemodes, "1 for Chosen Play or 2 for Continuous Play")

if game_mode == "1":
    message = "Chosen Play"
else:
    message = "Continuous Play"

print("You are playing {}\n".format(message))

# Checks if code is in Chosen Play, if so then asks for how many questions
if game_mode == "1":
    how_many_que = int(input("How many questions do you want? "))

question_num = 0
correct_num = 0
outcome = []
low = 1
high = 50
# Set up lists to generate randomly from
que_options = ["basic_facts", "basic_facts", "inequation"]
operators = ["+", "-", "x", "/"]

# While loop for main code goes here
keep_going = ""
while keep_going == "":

    question_counter = qq_statement("(☞ﾟヮﾟ)☞  Question {}  ☜(ﾟヮﾟ☜)   ".format(question_num + 1), "=")
    que_type = random.choice(que_options)

    # Variable "Question" is returned as either Correct or Incorrect a.k.a. the que_outcome
    if que_type == "basic_facts":
        question = basic_facts_q(random.choice(operators), random.randint(low, high), random.randint(low, high))
    else:
        question = inequation_q(random.randint(low, high), random.randint(low, high))

    # Adds variables to lists so that they can be printed as stats
    outcome.append(question)
    correct_num = outcome.count("Correct")

    # Checks the gamemode then responds accordingly
    if game_mode == "2":
        # When in continuous mode asks user to play again
        keep_going = input("Press <ENTER> to play again or any key to quit ")
    else:
        # When in chosen mode stops the loop when the num of questions is reached
        if how_many_que == (question_num + 1):
            keep_going = "stop"

    # Adds 1 to question number after every question
    question_num += 1

# Overall Game Stats are done here
list_count = 1
game_results = qq_statement("📊   Game Results   📊  ", "-")
print("You got {} / {} correct\n".format(correct_num, question_num))

for thing in outcome:
    print("Question {}: {}".format(list_count, thing))
    list_count += 1
