import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('gray')
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()

cars = CarManager()

screen.listen()
screen.onkeypress(player.move, 'Up')

game_is_on = True
i = 1
while game_is_on:
    time.sleep(0.05)
    screen.update()
    cars.new_car()
    cars.move()

    if player.is_at_finish_line():
        player.new_lvl()
        scoreboard.lvl_up()
        cars.lvl_up()

    for car in cars.cars:
        if player.distance(car) < 25:
            game_is_on = False
            screen.update()
            scoreboard.game_over()


screen.exitonclick()
