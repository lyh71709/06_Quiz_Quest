# Quiz Quest Component 1b - get user input for certain variables needed

# Difficulty Selection
difficulty_valid = False
high = 0

while difficulty_valid == False:
    difficulty = input("Difficulty (Easy, Normal or Hard): ").lower()
    if difficulty == "easy" or difficulty == "e":
        high = 10
        difficulty_valid = True
    elif difficulty == "normal" or difficulty == "n":
        high = 50
        difficulty_valid = True
    elif difficulty == "hard" or difficulty == "h":
        high = 100
        difficulty_valid = True
    else:
        print("You didn't enter any of the difficulties")
        print()
        continue
    print(high)
