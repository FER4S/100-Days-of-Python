from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.new_lvl()

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def new_lvl(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
