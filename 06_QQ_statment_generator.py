# QQ Component 7 - Statement generator

# Make a function for statement generation
def qq_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

# Set the variable for question counter statements
question_num = 1

# Makes a correct statement
correct = qq_statement("✔✔✔   You got it!   ✔✔✔   ", "-")

print()
# Makes an incorrect statement
incorrect = qq_statement("❌❌❌   You got it wrong   ❌❌❌     ", "-")

print()
# Makes a game results statement
game_results = qq_statement("📊   Game Results   📊  ", "-")

print()
# Makes a question counter statement
# For loop to test if the question num changes
for item in range(0,3):
    question_counter = qq_statement("(☞ﾟヮﾟ)☞  Question {}  ☜(ﾟヮﾟ☜)   ".format(question_num), "=")
    question_num += 1
