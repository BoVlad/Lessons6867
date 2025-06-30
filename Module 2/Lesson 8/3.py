# os.mkdir("нова_папка") - створення папки у поточному каталозі
# os.rename("старий_файл.txt", "новий_файл.txt") - перейменування файлу
# os.remove("файл.txt") - видалення файлу
# os.getcwd() - дізнатися, де зараз знаходиться скрипт (current working directory)


import os

# os.mkdir("Vlad")
# os.rename("index.txt", "new_index.txt")
# os.remove("new_index.txt")
# print(os.getcwd())

# with open("index.txt", "w", encoding="utf-8"):         # with open("index.txt", "w", encoding="utf-8") as jopa:
#     print()


# r	- Читання з файлу. Файл повинен існувати.
# w	- Запис у файл. Створює новий файл або перезаписує існуючий.
# a	- Додавання в кінець файлу. Створює новий файл, якщо не існує.
# r+ - Читання та запис у файл. Файл повинен існувати.
# w+ - Читання та запис. Створює новий файл або перезаписує існуючий.
# a+ - Читання та додавання. Створює новий файл, якщо не існує.


# with open("index.txt", "r", encoding="utf-8") as file:
#     info = file.read()  # info = file.readline()
#     print(info)
#
# with open("index.txt", "w", encoding="utf-8") as file:      # "w" - перезаписати, "a" - додати.
#     file.write("Hello World\n")
#     file.write("Hello World\n")
#     file.write("Hello World\n")

with open("index.txt", "r", encoding="utf-8") as file:      # "w" - перезаписати, "a" - додати.
    answer = file.readlines()

print(answer)

sum = 0
for a in answer:
    print(a)
    sum = sum + 1

print(sum)
print(len(answer))


