from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Mile to KM Converter")
frame = ttk.Frame(root, padding=10)
frame.grid()

entry = ttk.Entry(frame)
entry.grid(column=1, row=0)

km_label=ttk.Label(frame, text="0")
km_label.grid(column=1, row=1)

def convert_miles_to_km()
    mile = float(entry.get())
    km_label.config(text=mile * 1.609344)

ttk.Label(frame, text="Miles").grid(column=2, row=0)
ttk.Label(frame, text="is equal to").grid(column=0, row=1)
ttk.Label(frame, text="Km").grid(column=2, row=1)
ttk.Button(frame, text="calculate", command=convert_miles_to_km).grid(column=1, row=2)

root.mainloop()