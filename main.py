from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize instances of CoffeeMaker, Menu, and MoneyMachine
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
available_drinks = menu.get_items()

is_on = True
while is_on:
    choice = input("What would you like to have? " + available_drinks)
    if choice == "report":
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        cost = drink.cost  # Call payment function once
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(drink)



