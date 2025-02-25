import random
from turtle import Turtle

class Food:
    def __init__(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.coordinates = (x, y)
        t = Turtle()
        t.penup()
        t.goto(x, y)
        t.shape("circle")
        t.color("white")
        self.__t__ = t

    def move(self, snake):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.coordinates = (x, y)
        self.__t__.goto(x, y)

    def set_coord(self, x_coord, y_coord):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.coordinates = (x, y)
