import random
from turtle import Turtle

from common import SCREEN_HEIGHT, SQUARE_SIZE


def __get_random_vector_value__():
    return 20 * random.choice([-1, 1])


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_modifier = None
        self.x_modifier = None
        self.penup()
        self.color("white")
        self.shape("square")
        self.set_moving_vector()

    def move(self):
        new_x = self.xcor() + self.x_modifier
        new_y = self.ycor() + self.y_modifier
        self.goto((new_x, new_y))

    def bounce_x(self):
        self.x_modifier *= -1

    def bounce_y(self):
        self.y_modifier *= -1

    def restart(self):
        self.set_start_position()
        self.set_moving_vector()

    def set_moving_vector(self):
        self.x_modifier = __get_random_vector_value__()
        self.y_modifier = __get_random_vector_value__()

    def set_start_position(self):
        self.goto((0, random.randint(0, SCREEN_HEIGHT / SQUARE_SIZE) * random.choice([1, -1])))
