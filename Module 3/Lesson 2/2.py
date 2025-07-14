import tkinter as tk

root = tk.Tk()

root.title("My super window")
root.geometry("800x800")
# root.resizable(False, False)
root.minsize(600, 600)
root.maxsize(1000, 1000)

label2 = tk.Label(root, text="My first label",
                 font=("Bahnschrift", 20),
                 fg="green",
                 bg="pink",
                 padx=600)
label2.pack(expand=True)


root.mainloop()