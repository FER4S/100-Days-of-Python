from art import logo
import random
from replit import clear


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def dealCard():
    card = random.choice(cards)
    return card


def calculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(US, CS):
    if US == CS:
        return "Draw! 🥰"
    elif CS == 0:
        return "Lost!, Computer has a BLACKJACK 🥺"
    elif US == 0:
        return "Won!, ez BLACKJACK ❤️"
    elif US > 21:
        return "You went over, LOST!🥺"
    elif CS > 21:
        return "Computer went over, EZ WIN! 🥰"
    elif US > CS:
        return "You win! ❤️"
    else:
        return "You lose 💔"


def Blackjack():
    print(logo)

    userCards = []
    computerCards = []
    isDone = False

    for _ in range(2):
        userCards.append(dealCard())
        computerCards.append(dealCard())
    while not isDone:
        userScore = calculateScore(userCards)
        compScore = calculateScore(computerCards)

        print(f"Your cards: {userCards}, current score: {userScore}")
        print(f"Computer's first card: {computerCards[0]}")

        if userScore == 0 or compScore == 0 or userScore > 21:
            isDone = True
        else:
            anotherCard = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if anotherCard != 'y':
                isDone = True
            else:
                userCards.append(dealCard())

    while compScore != 0 and compScore < 17:
        computerCards.append(dealCard())
        compScore = calculateScore(computerCards)

    print(
        f'Your final hand is {userCards}, and your final score is {userScore}')
    print(
        f"Computer's final hand is {computerCards}, and his final score is {compScore}")
    print(compare(userScore, compScore))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower() == 'y':
    clear()
    Blackjack()
