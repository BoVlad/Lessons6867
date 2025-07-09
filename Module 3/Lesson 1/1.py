import tkinter as tk

root = tk.Tk() # Головне вікно

root.title("My super window")
root.geometry("500x500")

label = tk.Label(root, text="My first label",
                 font=("Arial", 32),
                 fg="blue",
                 bg="yellow")
label.pack()

label2 = tk.Label(root, text="My first label",
                 font=("Bahnschrift", 32),
                 fg="green",
                 bg="pink")
label2.pack()

counter = 0
def info():
    global counter  # Імпорт змінної
    print(f"Кнопка натиснута {counter} разів")
    counter = counter + 1
    text = str(counter)
    label = tk.Label(root, text=counter,
                 font=("Arial", 32),
                 fg="blue",
                 bg="yellow")
    label.pack()

def lab2yell():
    global label2
    label2 = label2.config(fg="yellow")
    label2.pack()

button = tk.Button(root, text="Натисни мене", command=info)
button.pack()

button2 = tk.Button(root, text="Не натисни мене", command=lab2yell)
button2.pack()

def showtext():
    text = entry.get()
    print(f"Введено: {text}")

entry = tk.Entry(root)
entry.pack()

button3 = button = tk.Button(root, text="Показати текст", command=showtext)
button3.pack()

root.mainloop()   # Незкінченний цикл для програми