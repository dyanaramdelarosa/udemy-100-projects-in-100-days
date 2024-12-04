"""
Day 5 Project (Loops): Password Generator

This project showcases the use of loops in a password generator project
"""

import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# ctr_letters = ctr_symbols = ctr_numbers = 0
# password_length = nr_letters + nr_symbols + nr_numbers
# password = []
#
# for i in range(0, password_length):
#     possible_value = []
#     if ctr_letters < nr_letters:
#         possible_value.append(0)
#     if ctr_symbols < nr_symbols:
#         possible_value.append(1)
#     if ctr_numbers < nr_numbers:
#         possible_value.append(2)
#
#     if len(possible_value) == 0:
#         break
#
#     char_type = random.choice(possible_value)
#     if char_type == 0:
#         password.append(random.choice(letters))
#         ctr_letters += 1
#     elif char_type == 1:
#         password.append(random.choice(symbols))
#         ctr_symbols += 1
#     else:
#         password.append(random.choice(numbers))
#         ctr_numbers += 1

password = []
for _ in range(0, nr_letters):
    password.append(random.choice(letters))

for _ in range(0, nr_symbols):
    password.append(random.choice(symbols))

for _ in range(0, nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)

print(password)
print("".join(password))
