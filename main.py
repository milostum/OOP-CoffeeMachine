from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#     []            {}
MENU = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

turn_on = True
while turn_on:
    request = input(f"What would you like? ({MENU.get_items()}): ")
    if request == "off":
        break
    elif request == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        find_object = MENU.find_drink(request)
        if request in ["espresso", "latte", "cappuccino"]:
            name = find_object.name
            water = find_object.ingredients["water"]
            milk = find_object.ingredients["milk"]
            coffee = find_object.ingredients["coffee"]
            cost = find_object.cost
            item = MenuItem(name, water, milk, coffee, cost)

            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)
                    money_machine.money_received = 0
