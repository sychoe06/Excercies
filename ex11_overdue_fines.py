def overdue_fine(days_overdue_):
    base_charge = 0.5
    daily_charge = 0.8
    max_charge = 30
    gross_charge = base_charge + (days_overdue_ * daily_charge)
    if gross_charge > 30:
        fine = max_charge
    else:
        fine = gross_charge
    return fine


# Main routine
days_overdue = int(input("Enter days overdue: "))
print(f"Fine is ${(overdue_fine(days_overdue)):,.2f}")
