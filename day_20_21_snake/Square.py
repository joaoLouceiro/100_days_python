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

    def set_coord(self, x_coord, y_coord):
        self.__square__.setx(x_coord)
        self.__square__.sety(y_coord)

    def get_x(self):
        return self.__square__.xcor()

    def get_y(self):
        return self.__square__.ycor()
