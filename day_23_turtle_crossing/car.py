from turtle import Turtle


class Car(Turtle):
    def __init__(self, coord, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.goto(coord)
        self.seth(180)
        self.shapesize(stretch_len=2)

    def move(self, speed):
        self.fd(speed)

    def detect_collision(self, player):
        return  self.ycor() - 10 <= player.ycor() <= self.ycor() + 10 and self.distance(player) < 30