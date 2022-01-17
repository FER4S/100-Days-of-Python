from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep
from blocks import Blocks


screen = Screen()
screen.setup(600, 700)
screen.title('Break Out')
screen.bgcolor('#000')
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkeypress(paddle.go_left, 'Left')
screen.onkeypress(paddle.go_right, 'Right')

ball = Ball()

scoreboard = Scoreboard()

blocks = Blocks()

playing = True
while playing:
    screen.update()
    ball.move()
    sleep(ball.move_speed)

    if ball.xcor() < -280 or ball.xcor() > 275:
        ball.bounce_x()

    if ball.ycor() < -290 and ball.distance(paddle) < 50:
        # if ball.xcor() > paddle.xcor():
        #     ball.bounce_x()
        ball.bounce_y()
        ball.speed_up()
        scoreboard.combo_up()

    if ball.ycor() > 330:
        ball.bounce_y()

    if ball.ycor() < -315 and ball.distance(paddle) > 50:
        scoreboard.combo_down()
        ball.reset_ball()

    blocks_left = 44
    for block in blocks.blocks:
        if block.xcor() == 6969:
            blocks_left -= 1
            if blocks_left == 0:
                scoreboard.game_over()
                playing = False
        if ball.distance(block) < 30 and (ball.ycor() < block.ycor() or ball.ycor() > block.ycor()):
            ball.bounce_y()
            block.goto(6969, 6969)
            scoreboard.add_score()
            scoreboard.refresh()
        if ball.distance(block) < 40 and ball.ycor() == block.ycor():
            ball.bounce_x()
            block.goto(6969, 6969)
            scoreboard.add_score()
            scoreboard.refresh()

screen.exitonclick()
