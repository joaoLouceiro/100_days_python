from turtle import Turtle


class Score:
    def __init__(self):
        self.score = 0
        t = Turtle()
        t.penup()
        self.__t__ = t
        self.__write_score__()

    def __write_score__(self):
        t = self.__t__
        t.reset()
        t.sety(270)
        t.color("white")
        t.write(f"Score = {self.score}", align="center", font=('Arial', 16, 'normal'))
        t.color("black")
        t.hideturtle()

    def increase_score(self):
        self.score += 1
        self.__write_score__()
