import tkinter as tk

root = tk.Tk()

root.title("My super window")
root.geometry("500x500")

label = tk.Label(root, text="", fg="white")
label.pack()

entry = tk.Entry(root, bg="blue4", fg="white")
entry.pack()

def checking():
    entrytext = entry.get()
    if entrytext == "Vlad" or entrytext == "Влад":
        label.config(text="Привіт розробник!", bg="red")
        label.pack()
    elif entrytext == "Matviy" or entrytext == "Матвій":
        label.config(text="Тобі тут не раді!", bg="red")
        label.pack()
    else:
        label.config(text="Привіт!", bg="red")
        label.pack()
    return

button = tk.Button(root, text="Натисніть для перевірки", command=checking)
button.pack()

root.mainloop()