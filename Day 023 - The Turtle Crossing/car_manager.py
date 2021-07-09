from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "pink", "blue", "purple", 'black', 'cyan']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.lvl = 0

    def new_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle('square')
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            x = 300
            y = random.randint(-250, 250)
            car.goto(x, y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + self.lvl * MOVE_INCREMENT)

    def lvl_up(self):
        self.lvl += 1


