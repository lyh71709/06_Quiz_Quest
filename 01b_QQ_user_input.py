# Quiz Quest Component 1b - get user input for certain variables needed

# While loop that loops until the input is valid
valid = False
while not valid:
    answer = input("Yes or No: ").lower()
    if answer == "yes" or answer == "y":
        # when it is yes or y
        print("YES")
        valid = True
    elif answer == "no" or answer == "n":
        # when it is no or n
        print("NO")
        valid = True
    else:
        # Error message
        print("Please enter either yes or no")
