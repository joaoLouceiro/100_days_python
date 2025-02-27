from turtle import Turtle, Screen

from common import SCREEN_WIDTH, SCREEN_HEIGHT
class MainScreen:
    def __init__(self):
        screen = Screen()
        screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        screen.bgcolor("black")
        screen.title("Pong")
        screen.tracer(0)
        self.__screen__ = screen

        dash = Turtle()
        dash.color("white")
        dash.penup()
        dash.width(5)
        dash.hideturtle()
        dash.goto(0, -SCREEN_HEIGHT / 2)
        dash.setheading(90)
        while dash.ycor() < SCREEN_HEIGHT / 2:
            dash.pendown()
            dash.fd(20)
            dash.penup()
            dash.fd(25)


    def update(self):
        self.__screen__.update()

    def listen(self):
        self.__screen__.listen()

    def onkeypress(self, fun, key):
        print("press")
        self.__screen__.onkeypress(fun, key)

    def terminate(self):
        self.__screen__.exitonclick()
