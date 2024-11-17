"""
Day 2 Project: Tip Calculator

This project calculates how much each person would have to pay given a
bill and a tip amount shared by n people.
"""


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
share = bill * (1 + tip_percentage) / num_people
print(f"Each person should pay: ${round(share, 2):.2f}")
