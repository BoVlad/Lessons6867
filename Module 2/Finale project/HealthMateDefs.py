import time
menu_visual ="""--- HealthMate ---
1. Ввести дані за сьогодні
2. Показати статистику
3. Вивести HI (HealthIndex)
4. Вийти
"""

def startmakefile():
    try:
        with open("HealthLog.txt", "r", encoding="utf-8") as file:
            filestart = file.readlines()
    except FileNotFoundError:
        with open("HealthLog.txt", "a", encoding="utf-8") as file:
            file.write("1\n")
            file.write("\n")
            file.write("\n")



# def fileupdate(time_basic):
#     with open('file.txt', 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#     with open("HealthLog.txt", "w", encoding="utf-8") as file:
#         lines[0] = file.write(f"{time_basic}\n")
#     return



def choice1(time_now):
    with open("HealthLog.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        time_basic = lines[0].replace("\n", "")
    if int(time_now) - int(time_basic) >= 64800:  # 64800
        print("Ви вибрали ввести дані за сьогодні. Повернутися в меню - 0, це не збереже ваші подальші записи. Якщо ви, можливо, щось не зробили, можете написати 1.")

        hours_sleep = input("Введіть години сну: ")
        while not hours_sleep.isdigit():
            print("Ви не ввели цифру або конкретний пункт меню. Спробуйте ще раз.")
            hours_sleep = input("Введіть години сну: ")
        hours_sleep = int(hours_sleep)
        if hours_sleep == 0:
            return

        glass_watter = input("Введіть скільки ви випили за сьогодні склянок води: ")
        while not glass_watter.isdigit():
            print("Ви не ввели цифру або конкретний пункт меню. Спробуйте ще раз.")
            glass_watter = input("Введіть скільки ви випили за сьогодні склянок води: ")
        glass_watter = int(glass_watter)
        if glass_watter == 0:
            return

        activity_minutes = input("Скільки сьогодні у вас було активності (хвилин): ")
        while not activity_minutes.isdigit():
            print("Ви не ввели цифру або конкретний пункт меню. Спробуйте ще раз.")
            activity_minutes = input("Скільки сьогодні у вас було активності (хвилин): ")
        activity_minutes = int(activity_minutes)
        if activity_minutes == 0:
            return

        while True:
            well_being = input("Ваше самопочуття (від 1 до 10): ")
            if not well_being.isdigit():
                print("Ви не ввели цифру або конкретний пункт меню. Спробуйте ще раз.")
                continue
            well_being = int(well_being)
            if well_being == 0:
                return
            if not 1 <= well_being <= 10:
                print("Ви не ввели цифру в потрібному діапазоні. Спробуйте ще раз.")
                continue
            break

        time_basic = int(time.time())

        with open('HealthLog.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        lines[0] = f"{time_basic}\n"
        lines[1] = "HItimed\n"

        with open("HealthLog.txt", "w", encoding="utf-8") as file:
            file.writelines(lines)

        with open("HealthLog.txt", "a", encoding="utf-8") as file:
            file.write(f"{hours_sleep}\n")
            file.write(f"{glass_watter}\n")
            file.write(f"{activity_minutes}\n")
            file.write(f"{well_being}\n")
        print("Дані успішно додано!")
        print()
        return
    else:
        print("Ой! На жаль час, після введення останніх даних не пройшов! Повертайтеся завтра!")
        print()
        print(int(time_now) - int(time_basic))
        return



def choice2():
    print("--- Статистика ---")
    with open('HealthLog.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    print("Статистика за сьогодні:")
    try:
        for i in lines[-10::]:
            print(i, end="")
    except:
        for i in lines[-5:-1]:
            print(i, end="")












