from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle((-350, 0), 'yellow')
r_paddle = Paddle((350, 0), 'pink')

screen.listen()
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')
screen.onkeypress(r_paddle.up, '8')
screen.onkeypress(r_paddle.down, '2')

ball = Ball()

scoreboard = Scoreboard()

is_on = True
while is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360 and ball.distance(r_paddle) > 50:
        ball.reset_position()
        scoreboard.l_scored()

    if ball.xcor() < -360 and ball.distance(l_paddle) > 50:
        ball.reset_position()
        scoreboard.r_scored()





screen.exitonclick()
