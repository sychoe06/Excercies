sound = 340/1000  # converting 340 m/s to km instead
count = float(input("Enter the number of seconds between the lightning and"
                    "thunder: "))
print("The distance of the storm is about", round(sound * count, 2), "km.")
