# Quiz Quest Component 1a - have an integer checking function

# Intcheck Function goes here
def intcheck(question):
    while True:
        try:
            response = int(input(question))
            return response
        # Error message
        except ValueError:
            print("Please enter an integer")
            continue

number = intcheck("Number: ")
print(number)