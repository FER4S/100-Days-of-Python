import random
from art import logo
from sys import exit

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

attempts = 0
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("INVALID INPUT!!!!")
    exit()


while attempts > 0:
    print(f'You have {attempts} attempts remaining to guess the number.')
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You are so good at gussing 🤯. The number was {number}.")
        exit()
    else:
        if guess > number:
            print("Too high!\nGuess again.")
        else:
            print("Too low!\nGuess again.")
        attempts -= 1
print("You've run out of guesses 😔, You lose!")
