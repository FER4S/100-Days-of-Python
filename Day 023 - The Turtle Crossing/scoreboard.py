from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.lvl = 1
        self.refresh()

    def lvl_up(self):
        self.lvl += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Level: {self.lvl}', align='center', font=FONT)
        
    def game_over(self):
        self.home()
        self.write('Game Over 😜', align='center', font=FONT)