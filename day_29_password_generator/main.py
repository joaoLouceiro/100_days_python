from tkinter import *
from tkinter import messagebox

INIT_MAIL = "mail@example.com"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    # Password Generator Project
    from random import choice, randint, shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    en_password.delete(0, END)
    en_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def on_press_add():
    site = en_website.get()
    user = en_username.get()
    password = en_password.get()

    if len(site) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showerror(title="Missing Fields", message="Please fill in all fields")
    else:
        confirm = messagebox.askokcancel(title=site, message=f"Details:\nEmail/User: {user}\nPassword: {password}\nIs it OK?")
        if confirm:
            with open("data.txt", "a") as data:
                data.write(f"{site} | {user} | {password}\n")

            en_website.delete(0, END)
            en_username.delete(0, END)
            en_username.insert(0, INIT_MAIL)
            en_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100 ,image=img)

canvas.grid(row=0, column=1)

Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

en_website = Entry(width=35)
en_website.grid(row=1, column=1, columnspan=2)
en_website.focus()

en_username = Entry(width=35)
en_username.grid(row=2, column=1, columnspan=2)
en_username.insert(0, INIT_MAIL)

en_password = Entry(width=22)
en_password.grid(row=3, column=1)

bt_generate = Button(text="Generate", command=generate)
bt_generate.grid(row=3, column=2)

bt_add = Button(text="Add", width=36, command=on_press_add)
bt_add.grid(row=4, column=1, columnspan=2)

window.mainloop()