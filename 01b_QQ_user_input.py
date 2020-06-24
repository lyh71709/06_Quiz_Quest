# Quiz Quest Component 1b - get user input for certain variables needed

# Difficulty Selection
difficulty_valid = False
high = 0
difficulty = input("Difficulty (Easy, Normal or Hard): ").lower()
if difficulty == "easy" or difficulty == "e":
    high = 10
else:
    print("You didn't enter any of the difficulties")
    print()
    print(high)
