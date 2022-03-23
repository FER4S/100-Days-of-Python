from turtle import Turtle, register_shape


class Player(Turtle):
    def __init__(self):
        super().__init__()
        register_shape('shapes/space-shuttle.gif')
        self.shape('shapes/space-shuttle.gif')
        self.penup()
        self.goto(0, -270)

    def move_left(self):
        new_x = self.xcor() - 20
        if new_x < -280:
            new_x = -280
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        if new_x > 280:
            new_x = 280
        self.goto(new_x, self.ycor())


