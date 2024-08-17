print("Welcome to the Tip calculator")

bill = float(input("What was the Total Bill ? "))

tip = int(input("What percentage tip would you like to give ? 10, 12, or 15? "))

split_among_people = int(input("How many people to split the bill? "))

tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage

final_bill = (bill + total_tip_amount) / split_among_people

print(f"Each person should pay : {round(final_bill,2)}")