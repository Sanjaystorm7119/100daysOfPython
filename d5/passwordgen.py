import random


print("Welcome to the Password Generator!")

#1 easy
# constants = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#               'u', 'v', 'w', 'x', 'y', 'z',
#               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
#               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#               'U', 'V', 'W', 'X', 'Y', 'Z',
#               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#               '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '_', '{', '}', '[', ']', ':', ';', '<', '>', '?', '/', '|', '\\', ',', '.', '~', '`']

# length = int(input("Enter password length: "))
# password = random.choices(constants, k=length)
# print("".join(password))

#2 custom
numberOfletters =  int(input("How many letters would you like in your password? "))
numberOfsymbols = int(input("How many symbols would you like? "))
numberOfnumbers = int(input("How many numbers would you like? "))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '_', '{', '}', '[', ']', ':', ';', '<', '>', '?', '/', '|', '\\', ',', '.', '~', '`']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password_list = []
for _ in range(numberOfletters):
    password_list.append(random.choice(letters))
for _ in range(numberOfsymbols):
    password_list.append(random.choice(symbols))
for _ in range(numberOfnumbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")
