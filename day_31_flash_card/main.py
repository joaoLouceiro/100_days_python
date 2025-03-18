from random import choice
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

game = None

def get_random_word():
    return choice(list(word_dict.items()))

def on_press_correct():
    global game
    window.after_cancel(game)
    if len(word_dict) > 0:
        word_dict.pop(word[0])
        start_game()

def on_press_wrong():
    global game
    if len(word_dict) > 0:
        window.after_cancel(game)
        start_game()


def flip_card():
    canvas.itemconfig(card, image=img_back)
    canvas.itemconfig(txt_lang, text="English")
    canvas.itemconfig(txt_word, text=word[1])

def start_game():
    global word, game
    if len(word_dict.keys()) > 0:
        word = get_random_word()
        canvas.itemconfig(card, image=img_front)
        canvas.itemconfig(txt_lang, text="French")
        canvas.itemconfig(txt_word, text=word[0])
        game = window.after(3000, flip_card)
    else:
        canvas.itemconfig(txt_lang, text="Congratulations!")
        canvas.itemconfig(txt_word, text="You got it!")
    print(len(word_dict.keys()))


word_dict = {row.French:row.English for (index, row) in pandas.read_csv("data/french_words.csv").iterrows()}
word = ""

window = Tk()
window.title("French Flash Card")
window.config(padx=50, pady=50)
img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")

canvas = Canvas()
canvas.config(height=526, width=800)
card = canvas.create_image(401, 263, image=img_front)

txt_lang= canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
txt_word= canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

img_correct = PhotoImage(file="images/right.png")
img_wrong = PhotoImage(file="images/wrong.png")

button_correct = Button(image=img_correct, highlightthickness=0, command=on_press_correct)
button_wrong = Button(image=img_wrong, highlightthickness=0, command=on_press_wrong)

button_correct.grid(row=1, column=0)
button_wrong.grid(row=1, column=1)



start_game()
window.mainloop()