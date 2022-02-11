def length_num_checker(question):
    length_error = "\nSorry, you must enter the length of the building"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(length_error)


def width_num_checker(question):
    width_error = "\nSorry, you must enter the width of the building\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(width_error)


DEPTH_1 = 0.25
DEPTH_2 = 0.5
total = 0
end_of_program = "False"
building_error = "ERROR!! Please enter only '1', '2' or 'x'!"


while end_of_program == "False":
    building_type = input("What is the type of the building?\n"
                          "'1' for Residential\n'2' for Commercial"
                          "\n'x' to finish\nEnter here: ").lower()
    if building_type == "1":
        length = length_num_checker("\nEnter the length of the building "
                                    "(in metres): ")
        width = width_num_checker("Enter the width of the building "
                                  "(in metres): ")
        volume_1 = length * width * DEPTH_1
        total += volume_1
        print("\nThe volume of concrete required for a slab with a length of",
              length, "and width of", width, "and a depth of", DEPTH_1, "is",
              volume_1, "cubic metres\n")
    elif building_type == "2":
        length = length_num_checker("\nEnter the length of the building "
                                    "(in metres): ")
        width = width_num_checker("Enter the width of the building "
                                  "(in metres): ")
        volume_2 = length * width * DEPTH_2
        total += volume_2
        print("\nThe volume of concrete required for a slab with a length of",
              length, "and width of", width, "and a depth of", DEPTH_2, "is",
              volume_2, "cubic metres\n")
    elif building_type == "x":
        print("- - - - - - - - - - - -")
        print("\nThe total amount of concrete needed for the day is", total)
        end_of_program = "yes"
    else:
        print(building_error + "\n")
