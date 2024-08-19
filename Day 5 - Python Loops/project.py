import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 
print("Welcome to the PyPassword Generator!") 

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))

user_password = ""

for i in range(0,nr_letters):
    user_password += random.choice(letters)

for i in range(nr_symbols):
    user_password += random.choice(symbols)

for i in range(nr_numbers):
    user_password += random.choice(numbers)

password_list = list(user_password)
random.shuffle(password_list)

user_password = ''.join(password_list)
print(user_password)

