# Назва бібліотеки	Призначення
# math - Математичні операції
# datetime - Робота з датами і часом
# random - Генерація випадкових чисел
# os - Взаємодія з операційною системою
# tkinter - Створення графічного інтерфейсу
# NumPy - Бібліотека для роботи з масивами і матрицями, надає чисельні функції.
# Pandas - Потужний інструмент для аналізу даних і роботи з таблицями.
# Matplotlib - Бібліотека для створення графіків і візуалізації даних.
# TensorFlow - Фреймворк для створення і навчання нейронних мереж, використовується в глибокому навчанні.

import math  # CTRL + ПКМ - подвитися що є в бібліотеці
print(math.sqrt(100))


import random as r
print(r.randint(0, 10))


import datetime as d
print(d.datetime.now().year)


import time
print(time.localtime().tm_hour)
time_now = time.localtime()
print(f"{time_now.tm_hour}:{time_now.tm_min}:{time_now.tm_sec}")



