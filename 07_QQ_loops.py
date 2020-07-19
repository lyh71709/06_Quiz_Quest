# Quiz Quest Component 8 - Allows users to choose between continuous play or chosen play

game_mode = int(input("1 or 2"))

if game_mode == 1:
    how_many_que = int(input("How many questions? "))

question_num = 0
keep_going = ""
while keep_going == "":

    # Main code goes here
    answer = input("Integer: ")
    question_num += 1
    if game_mode == 2:
        keep_going = input("Play Again?")
    elif game_mode == 1:
        if question_num == how_many_que:
            keep_going = "end"
