from replit import clear
from sys import exit
from art import logo


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def multi(x, y):
    return x*y


def div(x, y):
    return x/y


operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div,
}
while True:
    print(logo)

    x = float(input("What is the first number? "))

    keepGoing = True

    for key in operations:
        print(key)

    while keepGoing:

        operation = input("Pick an operation: ")

        y = float(input("What is the next number? "))

        function = operations[operation]
        result = function(x, y)
        print(f'{x} {operation} {y} = {result}')

        more = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'q' to quit the app: ").lower()
        if more == 'q':
            exit()
        elif more != 'y':
            keepGoing = False
            clear()
        x = result
