#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""
#
#
# for char in range(1,nr_letters + 1): #(0,nr_letters
#     #password += random.choice(letters)
#     random_character = random.choice(letters)
#     password = password+random_character
#
# for char in range(1,nr_symbols + 1):
#     password += random.choice(symbols)
#
# for char in range(1,nr_numbers + 1):
#     password += random.choice(numbers)
#
# print(password)

password_List = []


for char in range(1,nr_letters + 1): #(0,nr_letters
    #password += random.choice(letters)
    password_List.append(random.choice(letters))

for char in range(1,nr_symbols + 1):
    password_List.append(random.choice(symbols))

for char in range(1,nr_numbers + 1):
    password_List.append(random.choice(numbers))

print(password_List)
random.shuffle(password_List)
print(password_List)

password = ""
for char in password_List:
    password += char

print(f"Your Password is: {password}")
