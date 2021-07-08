from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos, color):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(color)
        self.shapesize(5, 1)
        self.goto(pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
