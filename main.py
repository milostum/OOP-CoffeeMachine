from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#     []            {}
MENU = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True
while is_on:
    options = MENU.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = MENU.find_drink(choice)
        if choice in ["espresso", "latte", "cappuccino"]:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                money_machine.money_received = 0
