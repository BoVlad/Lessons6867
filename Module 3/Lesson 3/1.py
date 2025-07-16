from tkinter import Tk, Label

def on_click(event):
    print(event)
    label.config(text="Мене натиснули")

root = Tk()
label = Label(root, text="натисни мене", bg="lightblue")
label.pack(pady=20, padx=20)

label.bind("<Button 1>", on_click)

root.mainloop()
