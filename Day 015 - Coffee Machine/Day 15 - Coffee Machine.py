from data import MENU, resources
from sys import exit


def check_resources(drink):
    water = drink['ingredients']['water']
    milk = drink['ingredients']['milk']
    coffee = drink['ingredients']['coffee']
    if water <= resources['water'] and milk <= resources['milk'] and coffee <= resources['coffee']:
        return True
    return False


def check_cost(drink, total):
    cost = drink["cost"]
    if total >= cost:
        return True
    return False


def make_drink(drink):
    water = drink['ingredients']['water']
    milk = drink['ingredients']['milk']
    coffee = drink['ingredients']['coffee']
    money = drink['cost']
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee
    resources['money'] += money


def coffee_machine():
    action = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if action == 'off':
        exit()
    elif action == 'report':
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${resources['money']}")
    elif action == 'espresso' or action == 'latte' or action == 'cappuccino':
        drink = MENU[action]
        if check_resources(drink):
            print("Please insert coins.")
            quarters = (int(input("How many quarters?: ")))*0.25
            dimes = int(input("How many dimes?: "))*0.1
            nickles = int(input("How many nickles?: "))*0.05
            pennies = int(input("How many pennies?: "))*0.01
            total = quarters + dimes + nickles + pennies
            if check_cost(drink, total):
                change = total - drink['cost']
                if change > 0:
                    print(f'Here is ${round(change, 2):.2f} in change.')
                make_drink(drink)
                print(f'Here is your {action} ☕, Enjoy! 🥰')
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Sorry, there is not enough water.")
    else:
        print('Invalid input!')


while True:
    coffee_machine()
