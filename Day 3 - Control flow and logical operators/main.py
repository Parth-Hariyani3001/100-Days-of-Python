# if and else
water_level = 50
if water_level > 80:
    print("Drain the water")
else:
    print("Let it fill up")


# modulo operator
print(5 % 2)


# Nested if else and elif
career = input("Have you completed your degree y/n ? ")
if career == "y":
    skill = input("Do you know DSA y/n ? ")
    if skill == "y":
        print("Welcome to our company")
    elif skill == "n":
        if input("Do you know MERN stack y/n ? ") == "y":
            print("Welcome to our company")
        else:
            print("We can't hire you sorry")
else:
    print("Please complete your Graduation")
