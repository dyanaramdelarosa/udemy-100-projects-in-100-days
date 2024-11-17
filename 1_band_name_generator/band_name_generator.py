"""
Day 1 Project: Band Name Generator

This project simply generates a band name suggestion by using
the user's personal details.
"""

print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")

print(f"Your band name could be {city_name.capitalize()} {pet_name.capitalize()}")
