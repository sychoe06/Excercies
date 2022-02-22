def sales_for_today():
    print("=" * 30)
    print("The Total tickets sold today was:", total_sold)
    print("This was made of up:\n" + str(adult_tickets), "for adults; and\n",
          str(student_tickets) + "for students; and",
          str(child_tickets), "for children; and",
          str(gift_voucher_tickets), "gift vouchers\n\n"
          "Sales for the day came to $", total_sales)


# Main routine
ADULT = 12.5
STUDENT = 9
CHILD = 7
GIFT_VOUCHER = 0

total_sold = 0
total_sales = 0
adult_tickets = 0
student_tickets = 0
child_tickets = 0
gift_voucher_tickets = 0

end_of_sales = "N"
sell_ticket = input("Do you want to sell a ticket? (Y/N): ").upper()
if sell_ticket == "Y":
    while end_of_sales == "N":
        type_of_ticket = input("What type of ticket do you want?\n"
                               "A for Adult, or\nS for Student, or\n"
                               "C for Child, or\nG for Gift voucher\n"
                               ">> ").upper()
        confirm = input("Confirm purchase of A ticket? (Y/N): ").upper()
        if confirm == "Y":
            total_sold += 1
            if type_of_ticket == "A":
                total_sales += ADULT
                adult_tickets += 1
            elif type_of_ticket == "S":
                total_sales += STUDENT
                student_tickets += 1
            elif type_of_ticket == "C":
                total_sales += CHILD
                child_tickets += 1
            elif type_of_ticket == "G":
                total_sales += GIFT_VOUCHER
                gift_voucher_tickets += 1
            print()
        else:
            print("The purchase of a ticket has been cancelled.\n")
        sell_ticket_again = input("Do you want to sell another ticket?"
                                  " (Y/N): ").upper()
        if sell_ticket_again == "N":
            end_of_sales = "Y"
            sales_for_today()

elif sell_ticket == "N":
    sales_for_today()
