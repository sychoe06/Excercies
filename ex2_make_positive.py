def make_positive(num_to_get_abs):
    abs_value = abs(num_to_get_abs)
    return abs_value


# main routine
number = int(input("Enter number: "))
print(f"The abs of {number} is: {make_positive(number)}")
