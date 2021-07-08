from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=("Courier", 20, "normal"))

    def game_over(self):
        self.home()
        self.write('Game Over! 😝', align='center', font=("Courier", 20, "normal"))
