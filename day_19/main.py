import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Color:")
colors = ["red", "orange", "green", "yellow", "blue", "purple" ]
tts = []

i = -90
for c in colors:
    t = Turtle()
    t.shape("turtle")
    t.color(c)
    t.penup()
    t.goto(x=-230, y=i)
    i += 30
    tts.append(t)

winner = ""
while winner == "" :
    t = random.choice(tts)
    t.fd(random.randint(1,10))
    if t.xcor() >= 230:
        winner = t.color()

if winner == user_bet:
    print("you won")
else:
    print("you lost")

screen.exitonclick()