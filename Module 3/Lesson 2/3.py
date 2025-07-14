from tkinter import Tk, Label, Button

root = Tk()
root.title("GUI з Pack")

header = Label(root,
               text="Це менбюфьббьс",
               bg="lightblue",
               fg="white",
               font=("Arial", 20),
               padx=10, pady=10)
header.pack(side="top",
            fill="x")

instruction = Label(root,
                    text="🗿",
                    bg="black",
                    fg="lime",
                    font=("Arial", 50),
                    padx=10, pady=10)
instruction.pack(side="top",
                 fill="x",
                 padx=100, pady=10)

left_button = Button(root,
                     text="La cnopca",
                     bg="orange", fg="white",
                     font=("Arial", 12),
                     padx=20, pady=10)
left_button.pack(side="left",
                 fill="y",
                 expand=True,
                 padx=10, pady=200)

right_button = Button(root,
                      text="Кнопка",
                      bg="purple",
                      fg="gray",
                      font=("Arial", 12),
                      padx=20, pady=10)
right_button.pack(side="right",
                  fill="y",
                  expand=True,
                  padx=10, pady=109)

status = Label(root,
               text="А мене забули видалити ",
               bg="black", fg="yellow",
               font=("Arial", 12),
               padx=10, pady=16)
status.pack(side="bottom",
            fill="x")

root.mainloop()