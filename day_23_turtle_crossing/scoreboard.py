from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.show_level()

    def show_level(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(-240, 240)
        self.write(f"Level = {self.score}", align="left", font=FONT)

    def update_level(self):
        self.score += 1
        self.show_level()
