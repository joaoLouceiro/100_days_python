import time
from  turtle import Screen, Turtle

from Snake import Snake

SCREEN_SIZE=600

screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Suna-ku")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")

while True:
    time.sleep(0.1)
    snake.move()
    screen.update()

screen.exitonclick()