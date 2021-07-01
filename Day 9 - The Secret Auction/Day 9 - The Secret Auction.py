from replit import clear
from art import logo

bidders = []


def add_bidder(name, bid):
    bidder = {}
    bidder["name"] = name
    bidder["bid"] = bid
    bidders.append(bidder)


print(logo)

more = True
while more:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    action = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    add_bidder(name, bid)

    if action == 'no':
        more = False
    clear()

maxbid = 0
maxname = ''

for dic in bidders:

    if dic["bid"] > maxbid:
        maxbid = dic["bid"]
        maxname = dic["name"]

print(f'The winner is {maxname} with a bid of ${maxbid}')
