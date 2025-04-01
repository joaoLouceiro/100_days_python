import random

from flask import Flask

url_numbers_gif = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGR2Z2Vvd3IzN2g2MXZra3ZqcWlkYXoxMjRjMW9xaDJ2OGxydXBoZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif"
url_too_low_gif = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
url_too_high_gif = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
url_correct_gif = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

app = Flask(__name__)
res = random.randint(0,9)

def make_img(url):
    return f"<img src={url} href={url}/>"

@app.route("/")
def hello_world():
    return ("<h1>Guess between 0 and 9</h1>"
            f"{make_img(url_numbers_gif)}")

@app.route("/<int:guess>")
def guess_page(guess):
    if guess < res:
        return ("<h1 style='color:blue'>Too low</h1>"
                f"{make_img(url_too_low_gif)}")
    if guess > res:
        return ("<h1 style='color:red'>Too high</h1>"
                f"{make_img(url_too_high_gif)}")
    if guess == res:
        return ("<h1 style='color:green'>Correct!</h1>"
                f"{make_img(url_correct_gif)}")
