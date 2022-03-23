from turtle import Turtle, register_shape


class Invaders:
    def __init__(self):
        self.invaders = []
        self.create_invaders()

    def create_invaders(self):
        x = -260
        y = 280
        for i in range(4):
            for j in range(9):
                invader = Turtle()
                register_shape('shapes/space-invader.gif')
                invader.shape('shapes/space-invader.gif')
                invader.penup()
                invader.goto(x, y)
                self.invaders.append(invader)
                x += 55
            y -= 30
            x = -260

    def move_h(self, direction):
        for invader in self.invaders:
            if direction == 'L':
                new_x = invader.xcor() - .5
                invader.goto(new_x, invader.ycor())
            elif direction == 'R':
                new_x = invader.xcor() + .5
                invader.goto(new_x, invader.ycor())

    def move_v(self, level):
        for invader in self.invaders:
            new_y = invader.ycor() - (10 * level)
            invader.goto(invader.xcor(), new_y)
