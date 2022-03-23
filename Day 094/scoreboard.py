from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.lives = 2
        self.score = 0
        self.refresh()

    def border(self):
        self.goto(-300, -300)
        self.pendown()
        for _ in range(4):
            self.forward(600)
            self.left(90)
        self.penup()

    def refresh(self):
        self.clear()
        self.color('#fff')
        self.border()
        self.goto(-300, 300)
        self.write(f'Score: {self.score}', font=FONT)
        self.goto(170, 300)
        self.write(f'Level: {self.level}', font=FONT)
        self.goto(-300, -330)
        self.color('red')
        self.write('❤ ' * self.lives, font=FONT)
        self.color('#fff')

    def level_up(self):
        self.level += 1
        self.refresh()

    def life_loss(self):
        self.lives -= 1
        self.refresh()

    def score_up(self):
        self.score += (self.level * 10)
        self.refresh()

    def game_over(self):
        self.home()
        self.color('#fff')
        self.write(f'Your Score is {self.score}, Great Job!💪', align='center', font=FONT)
