from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.print_score(0, 0)

    def print_score(self, p1_score, p2_score):
        self.reset()
        self.goto(0, 260)
        self.color("white")
        self.write(f"{p1_score}\t\t{p2_score}", align="Center", font=('Arial', 20, 'normal'))
        self.hideturtle()

