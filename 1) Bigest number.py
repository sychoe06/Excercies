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
while zero == "no":
    num_1 = integer_checker("First number: ")
    num_2 = integer_checker("Second number: ")
    if num_1 > num_2:
        print(num_1)
        if num_1 == 0:
            zero = "yes"
        elif num_2 == 0:
            zero = "yes"
        else:
            print()
    elif num_1 < num_2:
        print(num_2)
        if num_1 == 0:
            zero = "yes"
        elif num_2 == 0:
            zero = "yes"
        else:
            print()
    else:
        print("The two numbers are equal")
        if num_1 == 0:
            zero = "yes"
        elif num_2 == 0:
            zero = "yes"
        else:
            print()
