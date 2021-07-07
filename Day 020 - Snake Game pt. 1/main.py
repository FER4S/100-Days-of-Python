from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')


is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
