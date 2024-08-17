import random

choice_list = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

user_choice = int(
    input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))

comp_choice = random.randint(0, 2)

print(choice_list[user_choice])

print("Computer chose: ")

print(choice_list[comp_choice])

if (user_choice == comp_choice):
    print("It's a draw")
elif (user_choice == 0 and comp_choice == 2):
    print("you win")
elif (user_choice == 1 and comp_choice == 0):
    print("You win")
elif (user_choice == 2 and comp_choice == 1):
    print("You win")
else:
    print("You lose")
