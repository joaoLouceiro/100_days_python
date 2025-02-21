from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def get_user_selection():
    return input(f"Whatcha want? {menu.get_items()} ")

def print_report():
    coffee_maker.report()
    money_machine.report()

def can_make_drink(drink):
    return coffee_maker.is_resource_sufficient(drink)

def has_enough_funds(drink) :
    return money_machine.make_payment(drink.cost)

is_running = True
while is_running:
    u_sel = get_user_selection()
    if u_sel == 'off':
        is_running = False
        print("Shutting down")
    elif u_sel == "report":
        print_report()
    else:
        drink = menu.find_drink(u_sel)
        if drink is not None and can_make_drink(drink) and has_enough_funds(drink):
            coffee_maker.make_coffee(drink)

