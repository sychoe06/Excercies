# Integer checking function
def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# Main routine
zero = "no"
# Keeps asking for two numbers until one of the numbers is 0
while zero == "no":
    num_1 = integer_checker("First number: ")
    num_2 = integer_checker("Second number: ")
    # If the first number is bigger than the second number
    # it will print the first number
    if num_1 > num_2:
        print(num_1)
        # If either the first or second number = 0
        # then the code will stop looping
        if num_1 == 0:
            zero = "yes"
        elif num_2 == 0:
            zero = "yes"
        else:
            print()
    # If the second number is bigger than the first number
    # it will print the second number
    elif num_1 < num_2:
        print(num_2)
        if num_1 == 0:
            zero = "yes"
        elif num_2 == 0:
            zero = "yes"
        else:
            print()
    # However if no number is bigger than the other
    # it will say that both numbers are equal
    else:
        print("The two numbers are equal")
        if num_1 == 0:
            zero = "yes"
        elif num_2 == 0:
            zero = "yes"
        else:
            print()
