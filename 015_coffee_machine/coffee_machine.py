"""
Day 3 Project (Local Development Environment Setup): Coffee Machine

This project mimics how a coffe machine operates.
It has the following features:
    * Print report (coffee machine resources)
    * Make coffee
        * Check if resources are sufficient to make the drink
        * Check if coin payment is enough for the drink cost
        * Use coffee machine resources when making the drink
    * Turn off the coffee machine
"""

from collections.abc import Iterable

MENU: dict = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources: dict = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resource(drink: str, resource: str) -> bool:
    if resources[resource] < MENU[drink]["ingredients"].get(resource, 0):
        print(f"Sorry there is not enough {resource}.")
        return False
    return True


def drink_resources(drink: str) -> Iterable[bool]:
    yield check_resource(drink, "water")
    yield check_resource(drink, "milk")
    yield check_resource(drink, "coffee")


def check_resources(drink: str) -> bool:
    return all(resource for resource in drink_resources(drink))


def process_coins(drink) -> bool:
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    if total < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > MENU[drink]["cost"]:
        change = total - MENU[drink]["cost"]
        print(f"Here is ${change:.2f} in change.")

    resources["money"] += MENU[drink]["cost"]
    return True


def make_coffee(drink: str):
    resources["water"] -= MENU[drink]["ingredients"].get("water", 0)
    resources["milk"] -= MENU[drink]["ingredients"].get("milk", 0)
    resources["coffee"] -= MENU[drink]["ingredients"].get("coffee", 0)

    print(f"Here is your {drink}. Enjoy!")


def print_resources() -> None:
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def is_transaction_successful(choice):
    return check_resources(choice) and process_coins(choice)


def menu() -> None:
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        match choice:
            case "espresso" | "latte" | "cappuccino":
                if is_transaction_successful(choice):
                    make_coffee(choice)
            case "report":
                print_resources()
            case "off":
                return
            case _:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    menu()
