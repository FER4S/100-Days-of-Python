from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput('Make Your Bet', 'Which turtle will win the race? Enter a color: ').lower()

colors = ['red', 'purple', 'orange', 'yellow', 'green', 'blue']
turtles = []
y = -100
for turtle in range(6):
    new_turtle = Turtle('turtle')
    turtles.append(new_turtle)
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(-230, y)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        move_dist = random.randint(0, 10)
        turtle.forward(move_dist)
        if turtle.xcor() > 230:
            is_race_on = False
            turtle_won = turtle.pencolor()
            if turtle_won == user_bet:
                print("You've won the bet! ♥")
            else:
                print(f"You've lost the bet 😭, the winner is the {turtle_won} turtle.")
            turtle.goto(0, 0)
            turtle.write("I WON!", font=("Calibri", 60, "bold"))
            break
screen.exitonclick()
