"""
Day 16 Project (OOP): OOP Coffee Machine

Previous project's OOP implementation.
This project mimics how a coffee machine operates.
It has the following features:
    * Print report (coffee machine resources)
    * Make coffee
        * Check if resources are sufficient to make the drink
        * Check if coin payment is enough for the drink cost
        * Use coffee machine resources when making the drink
    * Turn off the coffee machine
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

if __name__ == "__main__":
    while True:
        choice = input(f"What would you like? ({menu.get_items()}): ")
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "off":
            break
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(
                drink
            ) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
