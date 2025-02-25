import time
import turtle
from  turtle import Screen, Turtle

from Food import Food
from Score import Score
from Snake import Snake
from common import SCREEN_SIZE

screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Suna-ku")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")

on_game = True
while on_game:
    time.sleep(0.1)
    snake.move()
    screen.update()
    if snake.head.coordinates == food.coordinates:
        snake.eat()
        food.move(snake)
        score.increase_score()
    for i in range(1,len(snake.body)):
        body_segment = snake.body[i]
        if snake.head.has_collided_with(body_segment):
            turtle.color("gray")
            turtle.write("Game over", align="center", font=('Arial', 16, 'bold'))
            turtle.hideturtle()
            on_game = False
            break
screen.exitonclick()