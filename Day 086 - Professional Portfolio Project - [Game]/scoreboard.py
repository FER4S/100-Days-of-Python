from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.combo = 1
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.color('#fff')
        self.goto(190, 315)
        self.write(f'Score: {self.score}', align='center', font=FONT)
        self.goto(-200, 315)
        self.color('red')
        self.write(f'Combo: X{self.combo}', align='center', font=FONT)

    def combo_up(self):
        self.combo += 1
        self.refresh()

    def combo_down(self):
        self.combo = 1
        self.refresh()

    def add_score(self):
        self.score += (self.combo * 10)

    # def show_add(self, pos):
    #     self.goto(pos)
    #     self.color('gold')
    #     self.write(f'+{self.combo * 10}!')

    def game_over(self):
        self.home()
        self.color('#fff')
        self.write(f'Your Score is {self.score}, Great Job!💪', align='center', font=FONT)

