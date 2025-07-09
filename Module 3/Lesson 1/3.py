import tkinter as tk
import random

colorlist = ["red", "orange", "yellow", "chartreuse3", "CadetBlue1", "blue4", "DarkOrchid"]

root = tk.Tk()

root.title("My super window")
root.geometry("500x500")

label = tk.Label(root, text="Натисни кнопку, щоб змінити колір фону!", font=("Bahnschrift", 15), bg="white")
label.pack()

def coloring():
    colornow = random.randint(0, 6)
    randomcolor = colorlist[colornow]
    root.config(bg=randomcolor)
    return

button = tk.Button(root, text="Магія", font=("Bahnschrift", 20), command=coloring, bg="white")
button.pack()

root.mainloop()