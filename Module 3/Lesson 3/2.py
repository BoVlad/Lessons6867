import tkinter as tk
import random

def change_background_color(event):
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F0E68C", "#FF33A1"]
    root.config(bg=random.choice(colors))

root = tk.Tk()

label = tk.Label(root, text="Натисни Enter щоб змінити колір фону", bg="lightblue", pady=50, padx=100)
label.pack(pady=100, padx=100)

label.bind_all("<Return>", change_background_color)

root.mainloop()

