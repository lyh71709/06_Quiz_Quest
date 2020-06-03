# Quiz Quest Component 1b - get user input for certain variables needed

# Difficulty Selection
difficulty = input("Difficulty (Easy, Normal or Hard): ").lower

if difficulty == "easy" or difficulty == "e":
    high = 10
elif difficulty == "normal" or difficulty == "n":
    high = 50
elif difficulty == "hard" or difficulty == "h":
    high = 100
