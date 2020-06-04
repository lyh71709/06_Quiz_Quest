# Quiz Quest Component 1c - get user input for certain variables needed (Trialling)

# String Checker
dif_range = ["hard", "normal", "easy"]

def str_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item
        error = print_list(to_check, len(to_check))
        print()

def print_list(list, length):
    statement = ""
    for i in range(0, length):
        if i == 0:
            statement = statement + " " + list[i]
        elif i == 1:
            statement = statement + ", " + list[i]
        else:
            statement = statement + ", {}.".format(list[i])
    print("Sorry, please enter one of{}".format(statement))

difficulty = str_checker("Difficulty (Easy, Normal or Hard): ",dif_range).lower()

if difficulty == "easy" or difficulty == "e":
    high = 10
elif difficulty == "normal" or difficulty == "n":
    high = 50
else:
    high = 100

print(high)