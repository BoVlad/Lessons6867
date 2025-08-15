import tkinter as tk

root = tk.Tk()

# Отримуємо розміри екрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Розраховуємо нові розміри вікна
new_width = screen_width // 2 # Половина ширини екрану
new_height = screen_height # Вся висота екрану

# Задаємо нові розміри вікна
root.geometry(f"{new_width}x{new_height}")

label1 = tk.Label(root,
                  text=f"Довжина вашого екрану: {screen_width}",
                  padx=10, pady=10,
                  bg="blue3", fg="white",
                  font=("Arial", 30, "bold"))
label1.pack(padx=20, pady=10)

label2 = tk.Label(root,
                  text=f"Ширина вашого екрану: {screen_height}",
                  padx=10, pady=10,
                  bg="blue4", fg="white",
                  font=("Arial", 30, "bold"))
label2.pack(padx=20, pady=10)
root.mainloop()