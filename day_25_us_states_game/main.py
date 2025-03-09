# did not take into account that the user might input the same answer twice.
# should check answer against an array of previously correctly answered states
import turtle
import pandas

screen= turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

score = 0
def right_answer(answer):
    global score
    score += 1
    row = data[data["state"] == answer]
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(row.x.values[0], row.y.values[0])
    t.write(answer)

while score <= 50:
    answer=screen.textinput(title=f"{score}/50 Guess the State", prompt="").title()
    if answer is None:
        break

    if answer in data["state"].to_list():
        right_answer(answer)

screen.mainloop()