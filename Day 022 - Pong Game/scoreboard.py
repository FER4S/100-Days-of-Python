from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.refresh_scoreboard()

    def l_scored(self):
        self.l_score += 1
        self.refresh_scoreboard()

    def r_scored(self):
        self.r_score += 1
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.color('white')
        self.write('Score', align='center', font=('Courier', 30, 'normal'))
        self.goto(-100, 250)
        self.color('yellow')
        self.write(self.l_score, align='center', font=('Courier', 24, 'normal'))
        self.goto(100, 250)
        self.color('pink')
        self.write(self.r_score, align='center', font=('Courier', 24, 'normal'))