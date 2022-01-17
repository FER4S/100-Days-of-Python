from turtle import Turtle
from random import choice

COLORS = ["orange", "yellow", "pink", "blue", 'cyan', 'darkgreen', 'chocolate', 'gray', 'lightgreen', 'maroon',
          'violet', 'magenta', 'purple', 'gold']


class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        x = -280
        y = 250
        # right = True
        for i in range(4):
            for j in range(11):
                block = Turtle('square')
                block.penup()
                block.shapesize(1, 2)
                block.color(choice(COLORS))
                block.goto(x, y)
                self.blocks.append(block)
                x += 55
                # if right:
                #     x += 55
                # else:
                #     x -= 55

            # if right:
            #     right = False
            # else:
            #     right = True
            y -= 30
            x = -280
