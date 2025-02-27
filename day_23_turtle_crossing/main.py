import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

p = Player()
screen.onkey(key="Up", fun=p.move)
cm = CarManager()
score = Scoreboard()
game_is_on = True

def next_level():
    time.sleep(2)
    p.go_to_start()
    time.sleep(1)
    cm.increase_speed()
    score.update_level()

def end_game():
    global game_is_on
    game_is_on = False

while game_is_on:
    time.sleep(0.1)
    cm.move_cars()
    screen.update()
    if p.reached_finish_line():
        next_level()
    if cm.detect_collision(p):
        end_game()



screen.mainloop()