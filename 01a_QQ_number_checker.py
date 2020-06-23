# Quiz Quest Component 1 - have an integer checking function


# Int_check Function goes here
def int_check(question):
    while True:
        try:
            response = int(input(question))
            return response

        # Error message
        except ValueError:
            print("Please enter an integer\n")
            continue

number = int_check("Number: ")
print(number)
