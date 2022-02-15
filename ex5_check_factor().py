def check_factor(num1, num2):
    if num1 % num2 == 0:
        print(f"{num2} is a factor of {num1}")
    elif num2 % num1 == 0:
        print(f"{num1} is a factor of {num2}")
    else:
        print(f"{num2} is NOT a factor of {num1}")


# main routine
num_1 = int(input("What is the first number: "))
num_2 = int(input("What is the second number: "))
check_factor(num_1, num_2)
