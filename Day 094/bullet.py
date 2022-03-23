from turtle import Turtle, register_shape


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.bullets = []
        self.invaders_bullets = []

    def fire(self, x, y):
        new_bullet = Turtle()
        register_shape('shapes/bullet-yellow.gif')
        new_bullet.shape('shapes/bullet-yellow.gif')
        new_bullet.setheading(90)
        new_bullet.penup()
        new_bullet.goto(x, y)
        self.bullets.append(new_bullet)

    def bullets_move(self):
        for bullet in self.bullets:
            bullet.forward(5)
        for bullet in self.invaders_bullets:
            bullet.forward(2.5)

    def invaders_fire(self, x, y):
        new_bullet = Turtle()
        register_shape('shapes/bullet-red.gif')
        new_bullet.shape('shapes/bullet-red.gif')
        new_bullet.setheading(270)
        new_bullet.penup()
        new_bullet.goto(x, y)
        self.invaders_bullets.append(new_bullet)
