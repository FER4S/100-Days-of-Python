from turtle import Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        x = 0
        for i in range(3):
            new_part = Turtle("square")
            new_part.penup()
            new_part.color('white')
            new_part.goto(x, 0)
            x -= 20
            self.snake_parts.append(new_part)

    def move(self):
        for part_number in range(len(self.snake_parts) - 1, 0, -1):
            next_pos = self.snake_parts[part_number - 1].position()
            self.snake_parts[part_number].goto(next_pos)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
