from turtle import Turtle


class Square:
    def __init__(self, x_coord = 0, y_coord = 0):
        turtle = Turtle()
        turtle.shape("square")
        turtle.penup()
        turtle.color("white")
        turtle.setx(x_coord)
        turtle.sety(y_coord)
        self.__square__ = turtle
        self.coordinates = (x_coord, y_coord)

    def set_coord(self, x_coord, y_coord):
        self.__square__.goto(x_coord, y_coord)
        self.coordinates = (x_coord, y_coord)

    def get_x(self):
        return self.__square__.xcor()

    def get_y(self):
        return self.__square__.ycor()

    def has_collided_with(self, other_square):
        return self.coordinates == other_square.coordinates
