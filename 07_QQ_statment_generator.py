# QQ Component 7 - Statement generator

def qq_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

question_num = 1

correct = qq_statement("✔✔✔   You got it!   ✔✔✔   ", "-")

print()
incorrect = qq_statement("❌❌❌   You got it wrong   ❌❌❌     ", "-")

print()
game_results = qq_statement("📊   Game Results   📊  ", "-")

print()
for item in range(0,3):
    question_counter = qq_statement("(☞ﾟヮﾟ)☞  Question {}  ☜(ﾟヮﾟ☜)   ".format(question_num), "-")
    question_num += 1