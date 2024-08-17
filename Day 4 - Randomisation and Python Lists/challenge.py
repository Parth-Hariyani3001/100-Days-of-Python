import random

friends = ["John","Bob","Charlie","Alice","Johhny"]

# First implementaion
# random_num = random.randint(0,len(friends) - 1)
# print(f"{friends[random_num]} will pay the bill today")

# Second implementation
print(random.choice(friends) + " Will pay the bill")