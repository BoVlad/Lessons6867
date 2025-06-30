try:
    with open("doings.txt", "r", encoding="utf-8") as file:
        filestart = file.readlines()
except:
    with open("doings.txt", "w", encoding="utf-8"):
        print()

print("ПРОГРАМА ДЛЯ ОБЛІКУ СПРАВ")

menu_visual = """Меню:
    1 - Показати всі справи
    2 - Додати нову справу
    3 - Очистити всі справи
    4 - Вийти з програми"""

menu3_visual = """Ви точно хочете видалити всі ваші справи? Їх буде неможливо повернути.
1. Так
2. Ні"""

while True:
    print(menu_visual)
    print()
    choice = input("Введіть ваш вибір: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            print("Ось ваші справи:")
            with open("doings.txt", "r", encoding="utf-8") as file:
                file_reader = file.readlines()
            listnum = 1
            for i in file_reader:
                print(f"{listnum}. {i}", end="")
                listnum = listnum + 1
            print()
        if choice == 2:
            new_doing = input("Введіть назву справи: ")
            with open("doings.txt", "a", encoding="utf-8") as file:
                file.write(f"{new_doing}\n")
            print("Справу успішно додано!")
            print()
        if choice == 3:
            print(menu3_visual)
            print()
            choice3 = input("Введіть ваш вибір: ")
            if choice3.isdigit():
                choice3 = int(choice3)
                if choice3 == 1:
                    with open("doings.txt", "w", encoding="utf-8"):
                        print()
                    print("Було видалено усі справи!")
                    print()
                if choice3 == 2:
                    print("Видалення всіх справ успішно скасоване!")
                    print()
            else:
                print("Ви не ввели цифру! Спробуйте ще раз.")
        if choice == 4:
            break
        else:
            print("Такого вибору немає. Введіть один з пунктів.")
    else:
        print("Ви не ввели цифру! Спробуйте ще раз.")


