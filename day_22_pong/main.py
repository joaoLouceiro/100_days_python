import time
from turtle import Screen

import ball
import myScreen
import score
from common import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

player_right = Player((350, 0))
player_left = Player((-350, 0))
screen = myScreen.MainScreen()
ball = ball.Ball()
score = score.Score()
screen.listen()
screen.onkeypress(key="Left", fun=player_right.move_down)
screen.onkeypress(key="Right", fun=player_right.move_up)
screen.onkeypress(key="a", fun=player_left.move_down)
screen.onkeypress(key="e", fun=player_left.move_up)


def restart():
    global player_right, player_left
    player_right.goto(350, 0)
    player_left.goto(-350, 0)
    ball.goto(0, 0)


def point_scored(player):
    global score
    player.score += 1
    score.print_score(player_left.score, player_right.score)
    time.sleep(3)
    restart()
    screen.update()
    time.sleep(3)
    ball.restart()


while True:
    time.sleep(0.1)
    ball.move()
    if ball.ycor() >= SCREEN_HEIGHT / 2 - 20 or ball.ycor() <= -SCREEN_HEIGHT / 2 + 20:
        ball.bounce_y()

    if ball.xcor() >= 340 and ball.distance(player_right) < 50 or ball.xcor() <= -340 and ball.distance(
            player_left) < 50:
        ball.bounce_x()

    if ball.xcor() >= 380:
        point_scored(player_left)

    if ball.xcor() <= -380:
        point_scored(player_right)
    screen.update()

screen.terminate()
