from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align='center', font=("Courier", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.refresh()

    # def game_over(self):
    #     self.home()
    #     self.write('Game Over! 😝', align='center', font=("Courier", 20, "normal"))
