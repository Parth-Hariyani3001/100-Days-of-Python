import os
from art import logo

print(logo)
is_bidding = True
users = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


while is_bidding:
    user_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))

    user = {
        "user_name": user_name,
        "bid_amount": bid_amount
    }
    users.append(user)

    choice = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if (choice == "yes"):
        clear_screen()
    elif (choice == "no"):
        highest_bidder = ""
        highest_bid_amount = 0
        for i in users:
            if i["bid_amount"] > highest_bid_amount:
                highest_bidder = i["user_name"]
                highest_bid_amount = i["bid_amount"]
        print(f"The Winner is {highest_bidder} with a bid of ${
              highest_bid_amount}")
        is_bidding = False
