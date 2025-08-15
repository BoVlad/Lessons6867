import tkinter as tk


root = tk.Tk()
root.title("Мій додаток")


menubar =tk.Menu(root)


file_menu1 =tk.Menu(menubar, tearoff=0)
file_menu1.add_command(label="Відкрити")
file_menu1.add_command(label="Зберегти")
file_menu1.add_command(label="Вийти", command=root.quit)


menubar.add_cascade(label="Змінити колір", menu=file_menu1)


root.config(menu=menubar)

root.mainloop()