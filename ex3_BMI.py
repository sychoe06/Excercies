def calc_bmi(bmi_to_check):
    if bmi_to_check < 18.5:
        result = "Underweight"
    elif bmi_to_check < 25:
        result = "Normal"
    elif bmi_to_check < 30:
        result = "Overweight"
    else:
        result = "Obese"
    return result


# main routine
bmi = float(input("Enter BMI: "))
print(calc_bmi(bmi))
