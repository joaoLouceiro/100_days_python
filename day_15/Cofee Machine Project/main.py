MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 10,
}
def coffee_machine():
    while True:
        u_input = get_user_input()
        if u_input == "off":
            print("Goodbye!")
            exit(0)
        elif u_input == "report":
            print_report()
        else:
            product = "espresso" if u_input == "e" else "latte" if u_input == "l" else "cappuccino"
            process_product(product)


def process_product(product):
    if machine_has_enough_resources(product):
        coins = get_coins()
        funds = get_user_funds(coins)
        if not user_has_enough_funds(funds, product):
            print("Not enough funds")
        else:
            resources["money"] += funds
            change = funds - MENU[product]['cost']
            if can_give_change(change):
                make_coffee(product)
                print(f"Change: {round(change, 2)}")
            else:
                resources["money"] -= funds
                print("Not enough change")

def machine_has_enough_resources(product):
    def check_resource(resource_name):
        resource_amount = resources.get(resource_name)
        product_resource_required = MENU[product]['ingredients'].get(resource_name) or 0
        has_enough = resource_amount >= resource_amount - product_resource_required
        if not has_enough:
            print(f"Not enough {resource_name}")
        return has_enough

    return check_resource('water') and check_resource('milk') and check_resource('coffee')

def get_coins():
    def get_coin(coin_name_inner):
        while not (amt := input(f"How many {coin_name_inner}? ")).isdigit():
            print("invalid value")
        return amt

    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }
    for coin_name in coins.keys():
        coins[coin_name] = int(get_coin(coin_name))
    return coins

def get_user_funds(u_coins):
    coin_values = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    total = 0

    for coin_name in u_coins.keys():
        total += u_coins[coin_name] * coin_values[coin_name]

    return total

def can_give_change(change):
    return change < resources["money"]

def make_coffee(product):
    for resource_name in resources.keys():
        resources[resource_name] -= MENU[product]["ingredients"].get(resource_name) or 0

    print(f"Here's your hot {product}!")

def user_has_enough_funds(funds, product):
    return funds >= MENU.get(product).get("cost")

def get_user_input():
    while (answer := input("What would you like? ([e]spresso/[l]atte/[c]appuccino) ")) not in ["e", "l", "c", "off", "report"]:
        print("invalid option")
    return answer

def print_report():
    print(f"Water:\t{resources['water']}ml\nMilk:\t{resources['milk']}ml\nCoffee:\t{resources['coffee']}g\nMoney:\t${resources.get('money', 0)}")

coffee_machine()

