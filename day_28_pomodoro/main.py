from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

def paint_checks():
    checks = ["\u2713" for c in range(0, reps // 2)]
    checkmark.config(text="".join(checks))


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    paint_checks()
    timer_title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_countdown():
    global reps
    if reps == 7:
        time = LONG_BREAK_MIN
        timer_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        timer_title.config(text="Work", fg=GREEN)
        time = WORK_MIN
    else:
        timer_title.config(text="Break", fg=PINK)
        time = SHORT_BREAK_MIN

    time *= 60
    if reps < 8:
        countdown(time)
        reps += 1
        paint_checks()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_countdown()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

img_file = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img_file)

timer_text = canvas.create_text(100, 134, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
timer_title = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 40, "bold"), fg=GREEN)

start_button = Button(text="Start", command=start_countdown)

reset_button = Button(text="Reset", command=reset)

checkmark = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))

timer_title.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
checkmark.grid(row=3, column=1)

window.mainloop()