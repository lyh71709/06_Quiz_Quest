# Quiz Quest Component 1b - get user input for certain variables needed

# Difficulty Selection
valid = False
while not valid:
    answer = input("Yes or No: ").lower()
    if answer == "yes" or answer == "y":
        print("YES")
        valid = True
    elif answer == "no" or answer == "n":
        print("NO")
        valid = True
    else:
        print("Please enter either yes or no")
