from art import logo, vs
from game_data import data
import random
from sys import exit
from replit import clear

print(logo)

score = 0


data_B = random.choice(data)
right = True
while right:
    data_A = data_B

    while data_A == data_B:
        data_B = random.choice(data)

    print(
        f'Compare A: {data_A["name"]}, a {data_A["description"]}, from {data_A["country"]}')
    print(vs)
    print(
        f'Against B: {data_B["name"]}, a {data_B["description"]}, from {data_B["country"]}')

    ans = input("Who has more followers? Type 'A' or 'B': ").lower()

    if data_A["follower_count"] > data_B["follower_count"]:
        right_ans = 'a'
    else:
        right_ans = 'b'

    if ans == right_ans:
        score += 1
        clear()
        print(logo)
        print(f"You're right!, Current score: {score}.")
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong!, Your final score: {score}")
        right = False
