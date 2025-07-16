import tkinter as tk
from tkinter import messagebox
import time

running = False
delay = 0

root = tk.Tk()
root.title("Auto Clicker")
root.geometry("350x300")
root.config(bg="#DFF7F8")
root.resizable(False, False)

Label1 = tk.Label(root,
                  text="AutoClicker",
                  fg="#057A72",
                  font=("Bahnschrift", 30),
                  bg="#DFF7F8")
Label1.place(relx=0.5, rely=0.1,
             anchor="center")


Label2 = tk.Label(root,
                  text="Кліків на секунду:",
                  fg="#057A72",
                  font=("Arial", 16),
                  bg="#DFF7F8")
Label2.place(relx=0.5, rely=0.35,
             anchor="center")


entry1 = tk.Entry(root,
                 font=("Arial", 16))
entry1.place(relx=0.5, rely=0.5,
             anchor="center")



def start_autoclicker():
    tk.messagebox.showinfo("AutoClicker", "Автоклікер запущено!")
    global running, delay
    clicks_per_second = int(entry1.get())
    delay = 1 / clicks_per_second
    running = True
    schedule_click()

def schedule_click():
    if running:
        print("Клац!")
        time.sleep(delay)
        schedule_click()

def stop_autoclicker():
    global running, delay
    running = False
    delay = 0
    tk.messagebox.showinfo("AutoClicker", "Автоклікер зупинено!")

def show_info(event):
    tk.messagebox.showinfo("AutoClicker", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")


Button1 = tk.Button(root,
                  text="Почати",
                  fg="white",
                  font=("Arial", 16),
                  bg="#4DAF51",
                  padx=20, pady=5,
                  command=start_autoclicker)

Button1.place(relx=0.3, rely=0.8,
             anchor="center")


Button2 = tk.Button(root,
                  text="Зупинити",
                  fg="white",
                  font=("Arial", 16),
                  bg="#F34235",
                  padx=10, pady=5,
                  command=stop_autoclicker)
Button2.place(relx=0.7, rely=0.8,
             anchor="center")


root.bind("i", show_info)

root.mainloop()