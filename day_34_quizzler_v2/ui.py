from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        window = Tk()
        window.title("Quizzler")
        window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        canvas = Canvas()
        canvas.config(width=300, height=250, background="white")
        self.question_text = canvas.create_text((150, 124), text="", width=280, font=("Arial", 20, "italic"))
        canvas.grid(row=1, column=0, columnspan=2, pady=20)

        img_true = PhotoImage(file="images/true.png")
        img_false = PhotoImage(file="images/false.png")
        btn_true = Button(image=img_true, highlightthickness=0, command=self.on_press_true)
        btn_false = Button(image=img_false, highlightthickness=0, command=self.on_press_false)

        btn_true.grid(row=2, column=0, pady=20)
        btn_false.grid(row=2, column=1, pady=20)

        self.btn_true = btn_true
        self.btn_false = btn_false
        self.canvas = canvas
        self.next_question()
        self.window = window
        window.mainloop()

    def on_press_true(self):
        self.display_answer(self.quiz_brain.check_answer("true"))

    def on_press_false(self):
        self.display_answer(self.quiz_brain.check_answer("false"))

    def display_answer(self, answer: bool):
        text = "Sorry, that's wrong"
        if answer:
            text = "You're right!"
        self.canvas.itemconfig(self.question_text, text=text)
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        self.btn_false.config(state="disabled")
        self.btn_true.config(state="disabled")

        self.window.after(1000, self.next_question)

    def next_question(self):
        self.btn_false.config(state="active")
        self.btn_true.config(state="active")
        self.canvas.itemconfig(self.question_text, text=self.quiz_brain.next_question())

