from turtle import Turtle

from common import SCREEN_HEIGHT, SQUARE_SIZE

class Player(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(coordinates)
        self.setheading(90)

    def move_up(self):
        if self.ycor()  < SCREEN_HEIGHT / 2 - SQUARE_SIZE * 3:
            self.fd(SQUARE_SIZE)

    def move_down(self):
        if self.ycor() > - SCREEN_HEIGHT / 2 + SQUARE_SIZE * 3:
            self.bk(SQUARE_SIZE)
