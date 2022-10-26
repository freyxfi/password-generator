#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the frey0x0 password generator!")
ps_letter = int(input(f"How many letters would you like to havein your passwd?\n"))

ps_symbols = int(input(f"How many symbols would you like to have in your passwd ? :-\n"))

ps_number = int(input(f"How many numbers would you like to have in ypur passwd:-\n"))

# Level - 1 

passwd = ""


for char in range(1,ps_letter + 1):
    passwd += random.choice(letters)

for char in range(1, ps_symbols + 1):
    passwd += random.choice(symbols)

for char in range(1, ps_number + 1):
    passwd += random.choice(numbers)

print(passwd)

