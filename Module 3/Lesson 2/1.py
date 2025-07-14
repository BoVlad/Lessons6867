import tkinter as tk

def main():
    root = tk.Tk ()
    root.title("Приклад фреймів з рамкою")

    # Перший фрейм (угорі)
    top_frame = tk.Frame(
        root,
        borderwidth=2,
        relief="groove",      # тип рамки: solid, groove, ridge, sunken, raised
        bg="#e0f7fa"         # колір фону для наочності
    )
    top_frame.pack(padx=10, pady=10, fill="both", expand=True)

    tk.Label(top_frame, text="Верхній фрейм").pack(pady=20)

    # Другий фрейм (унизу)
    bottom_frame = tk.Frame(
        root,
        borderwidth=2,
        relief="sunken",
        bg="#fff3e0"
    )
    bottom_frame.pack(padx=10, pady=(0, 10), fill="both", expand=True)

    tk.Label(bottom_frame, text="Нижній фрейм").pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()