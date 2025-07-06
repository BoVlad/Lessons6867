import time

menu_visual ="""--- HealthMate ---
1. 💻 Ввести дані за сьогодні
2. 📋 Показати статистику
3. 📈 Вивести поради для покращення стану
4. ❌ Скинути прогрес
5. 🚪 Вийти
"""

def startmakefile():
    try:
        with open("HealthLog.txt", "r", encoding="utf-8") as file:
            filestart = file.readlines()
    except FileNotFoundError:
        with open("HealthLog.txt", "w", encoding="utf-8") as file:
            file.write("1\n")
            file.write("\n")



def choice1(time_now):
    with open("HealthLog.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        time_basic = lines[0].replace("\n", "")
    if int(time_now) - int(time_basic) >= 64800:  # 64800
        print("💻 Ви вибрали ввести дані за сьогодні. Повернутися в меню - 0, це не збереже ваші подальші записи. Якщо ви, можливо, щось не зробили, можете написати 1.")
        while True:
            hours_sleep = input("🛌 Введіть години сну: ")
            if not hours_sleep.isdigit():
                print("❌ Ви не ввели цифру. Спробуйте ще раз.")
                continue
            hours_sleep = int(hours_sleep)
            if hours_sleep == 0:
                return
            if hours_sleep > 24:
                print("❌ Ви не могли спати більше ніж триває день! Введіть реальні години вашого сну.")
                continue
            break
        while True:
            glass_water = input("💧 Введіть скільки ви випили за сьогодні склянок води: ")
            if not glass_water.isdigit():
                print("❌ Ви не ввели цифру. Спробуйте ще раз.")
                continue
            glass_water = int(glass_water)
            if glass_water == 0:
                return
            if glass_water > 40:
                print("❌ Ви не могли випити стільки стаканів, це смертельна доза! Введіть реальну кількість випитих вами за сьогодні склянок води.")
                continue
            break
        while True:
            activity_minutes = input("🏃 Скільки сьогодні у вас було активності (хвилин): ")
            if not activity_minutes.isdigit():
                print("❌ Ви не ввели цифру. Спробуйте ще раз.")
                continue
            activity_minutes = int(activity_minutes)
            if activity_minutes == 0:
                return
            if activity_minutes > 420:
                print("❌ Ви не могли займатися стільки, це смертельна доза! Введіть реальний час в хвилинах ваших активностей.")
                continue
            break
        while True:
            well_being = input("🙆 Ваше самопочуття (від 1 до 10): ")
            if not well_being.isdigit():
                print("❌ Ви не ввели цифру. Спробуйте ще раз.")
                continue
            well_being = int(well_being)
            if well_being == 0:
                return
            if not 1 <= well_being <= 10:
                print("❌ Ви не ввели цифру в потрібному діапазоні. Спробуйте ще раз.")
                continue
            break
        time_basic = int(time.time())


        if 8 <= hours_sleep <= 12:
            sleep_score = 1.0
        elif hours_sleep < 8:
            sleep_score = (hours_sleep - 1) / 7
        else:
            sleep_score = (24 - hours_sleep) / 12

        if 8 <= glass_water <= 19:
            water_score = 1.0
        elif glass_water < 8:
            water_score = (glass_water - 1) / 7
        else:
            water_score = (40 - glass_water) / 21
        if 40 <= activity_minutes <= 200:
            activity_score = 1.0
        elif activity_minutes < 40:
            activity_score = (activity_minutes - 1) / 39
        else:
            activity_score = (420 - activity_minutes) / 220

        if 5 <= well_being <= 10:
            well_being_score = 1.0
        else:
            well_being_score = (well_being - 1) / 4

        HI = int(((sleep_score + water_score + activity_score + well_being_score) / 4) * 10)


        with open('HealthLog.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        lines[0] = f"{time_basic}\n"
        if lines[1].replace("\n", "") == "":
            lines[1] = f"{HI}\n"
        else:
            lines[1] = f"{lines[1].replace("\n", "")} {HI}\n"
        with open("HealthLog.txt", "w", encoding="utf-8") as file:
            file.writelines(lines)
        try:
            lines[-8] = lines[-4]
            lines[-7] = lines[-3]
            lines[-6] = lines[-2]
            lines[-5] = lines[-1]
            lines[-4] = f"{hours_sleep}\n"
            lines[-3] = f"{glass_water}\n"
            lines[-2] = f"{activity_minutes}\n"
            lines[-1] = f"{well_being}\n"
            with open("HealthLog.txt", "w", encoding="utf-8") as file:
                file.writelines(lines)
        except IndexError:
            with open("HealthLog.txt", "a", encoding="utf-8") as file:
                file.write(f"{hours_sleep}\n")
                file.write(f"{glass_water}\n")
                file.write(f"{activity_minutes}\n")
                file.write(f"{well_being}\n")
        print("✅ Дані успішно додано!")
        print()
        return
    else:
        print("Ой! На жаль час, після введення останніх даних не пройшов! Повертайтеся завтра!")
        print()
        return



def choice2():
    print("--- Статистика ---")
    with open('HealthLog.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    try:
        error = lines[-8]
        print("Статистика за передостанній день:")
        print(f"🛌 Ви спали годин: {lines[-8].replace("\n", "")}")
        print(f"💧  Ви випили склянок води: {lines[-7].replace("\n", "")}")
        print(f"🏃 У вас було хвилин активностей: {lines[-6].replace("\n", "")}")
        print(f"🙆 Ваше самопочуття на {lines[-5].replace("\n", "")} з 10")
        print("---")
        print("Статистика за останній день:")
        print(f"🛌 Ви спали годин: {lines[-4].replace("\n", "")}")
        print(f"💧  Ви випили склянок води: {lines[-3].replace("\n", "")}")
        print(f"🏃 У вас було хвилин активностей: {lines[-2].replace("\n", "")}")
        print(f"🙆 Ваше самопочуття на {lines[-1].replace("\n", "")} з 10")

        number = 0
        quantity = 0
        number_temp = ""
        for i in lines[1]:
            if i == " ":
                if number_temp != "":
                    quantity = quantity + 1
                    number = number + int(number_temp)
                    number_temp = ""
            else:
                number_temp = number_temp + i
        if number_temp != "":
            quantity = quantity + 1
            number = number + int(number_temp)
        print("---")
        print(f"💕 Ваш Health Index (HI) становить {number // quantity}")
        print(f"📅 Ви користуєтесь програмою днів: {quantity}")

    except IndexError:
        try:
            error = lines[-4]
            print("Статистика за передостанній день:")
            print("Статистики за вчора ще немає 🙁")
            print("---")
            print("Статистика за останній день:")
            print(f"🛌 Ви спали годин: {lines[-4].replace("\n", "")}")
            print(f"💧  Ви випили склянок води: {lines[-3].replace("\n", "")}")
            print(f"🏃 У вас було хвилин активностей: {lines[-2].replace("\n", "")}")
            print(f"🙆 Ваше самопочуття на {lines[-1].replace("\n", "")} з 10")
            print("---")
            print("📅 Ви користуєтесь програмою 1 день")
        except IndexError:
            print("На жаль, ви ще не ввели дані хоча би один раз. Введіть дані що би подивитися статистику!")
    print()



def choice3():
    print("--- Поради ---")
    with open('HealthLog.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    try:
        hours_sleep_yesterday = int(lines[-8].replace("\n", ""))
        glass_water_yesterday = int(lines[-7].replace("\n", ""))
        activity_minutes_yesterday = int(lines[-6].replace("\n", ""))
        well_being_yesterday = int(lines[-5].replace("\n", ""))
        hours_sleep = int(lines[-4].replace("\n", ""))
        glass_water = int(lines[-3].replace("\n", ""))
        activity_minutes = int(lines[-2].replace("\n", ""))
        well_being = int(lines[-1].replace("\n", ""))
        print("📊 Розберемо передостанній день:")
        if hours_sleep_yesterday < 8:
            print("🛌❌ Ви спали замало, треба спати більше!")
        if 8 <= hours_sleep_yesterday <= 12:
            print("🛌✅ Ваш сон в нормі! ")
        if hours_sleep_yesterday > 12:
            print("🛌❌ Ви спали забагато, треба спати менше!")
        if glass_water_yesterday < 7:
            print("💧❌ Ви випили замало, треба пити більше!")
        if 7 <= glass_water_yesterday <= 19:
            print("💧✅ Ваш водний баланс в нормі! ")
        if glass_water_yesterday > 19:
            print("💧❌ Ви випили забагато, треба пити менше!")
        if activity_minutes_yesterday < 40:
            print("🏃❌ Ваших активних занятть замало, активнічайте більше!")
        if 40 <= activity_minutes_yesterday <= 200:
            print("🏃✅ Кількість вашої активності в нормі! ")
        if activity_minutes_yesterday > 200:
            print("🏃❌ Ваших активних занятть забагато, активнічайте менше!")
        if well_being_yesterday < 5:
            print("🙆❌ Ви себе погано почували! Якщо морально, то підійміть собі настрій 🤗")
        if 5 <= well_being_yesterday <= 10:
            print("🙆✅ Ви себе добре почували! Це дуже круто!")

        print("---")
        print("📊 Розберемо останній день:")
        if hours_sleep < 8:
            print("🛌❌ Ви спали замало, треба спати більше!")
        if 8 <= hours_sleep <= 12:
            print("🛌✅ Ваш сон в нормі! ")
        if hours_sleep > 12:
            print("🛌❌ Ви спали забагато, треба спати менше!")
        if glass_water < 7:
            print("💧❌ Ви випили замало, треба пити більше!")
        if 7 <= glass_water <= 19:
            print("💧✅ Ваш водний баланс в нормі! ")
        if glass_water > 19:
            print("💧❌ Ви випили забагато, треба пити менше!")
        if activity_minutes < 40:
            print("🏃❌ Ваших активних занятть замало, активнічайте більше!")
        if 40 <= activity_minutes <= 200:
            print("🏃✅ Кількість вашої активності в нормі! ")
        if activity_minutes > 200:
            print("🏃❌ Ваших активних занятть забагато, активнічайте менше!")
        if well_being < 5:
            print("🙆❌ Ви себе погано почуваєте! Якщо морально, то підійміть собі настрій 🤗")
        if 5 <= well_being <= 10:
            print("🙆✅ Ви себе добре почуваєте! Це дуже круто!")


        print("---")
        print("📊 Підведемо підсумки:")

        number = 0
        quantity = 0
        number_temp = ""
        line2 = lines[1].replace("\n", "")
        for i in line2:
            if i == " ":
                if number_temp != "":
                    quantity = quantity + 1
                    number = number + int(number_temp)
                    number_temp = ""
            else:
                number_temp = number_temp + i
        if number_temp != "":
            quantity = quantity + 1
            number = number + int(number_temp)
        lines_line2_today = number / quantity

        number = 0
        quantity = 0
        number_temp = ""
        for i in line2[0:-3]:
            if i == " ":
                if number_temp != "":
                    quantity = quantity + 1
                    number = number + int(number_temp)
                    number_temp = ""
            else:
                number_temp = number_temp + i
        if number_temp != "":
            quantity = quantity + 1
            number = number + int(number_temp)
        lines_line2_yesterday = number / quantity

        if lines_line2_yesterday < lines_line2_today:
            print("📈 Ваш Health Index (HI) за останній день покращився! Так тримати!")
        if lines_line2_yesterday > lines_line2_today:
            print("📉 Ваш Health Index (HI) за останній день зменшився! Це погано, його треба підвищувати!")
        if lines_line2_yesterday == lines_line2_today:
            print("➖ Ваш Health Index (HI) за останні дні такий самий! Не погано і не добре!")
    except IndexError:
        try:
            hours_sleep = int(lines[-4].replace("\n", ""))
            glass_water = int(lines[-3].replace("\n", ""))
            activity_minutes = int(lines[-2].replace("\n", ""))
            well_being = int(lines[-1].replace("\n", ""))
            print("📊 Розберемо передостанній день день:")
            print("Порад за вчора ще немає 🙁")
            print("---")
            print("📊 Розберемо останній день:")
            if hours_sleep < 8:
                print("🛌❌ Ви спали замало, треба спати більше!")
            if 8 <= hours_sleep <= 12:
                print("🛌✅ Ваш сон в нормі! ")
            if hours_sleep > 12:
                print("🛌❌ Ви спали забагато, треба спати менше!")
            if glass_water < 7:
                print("💧❌ Ви випили замало, треба пити більше!")
            if 7 <= glass_water <= 19:
                print("💧✅ Ваш водний баланс в нормі! ")
            if glass_water > 19:
                print("💧❌ Ви випили забагато, треба пити менше!")
            if activity_minutes < 40:
                print("🏃❌ Ваших активних занятть замало, активнічайте більше!")
            if 40 <= activity_minutes <= 200:
                print("🏃✅ Кількість вашої активності в нормі! ")
            if activity_minutes > 200:
                print("🏃❌ Ваших активних занятть забагато, активнічайте менше!")
            if well_being < 5:
                print("🙆❌ Ви себе погано почуваєте! Якщо морально, то підійміть собі настрій 🤗")
            if 5 <= well_being <= 10:
                print("🙆✅ Ви себе добре почуваєте! Це дуже круто!")
        except IndexError:
            print("На жаль, ви ще не ввели дані хоча би один раз. Введіть дані що би подивитися поради!")
    print()



def choice4():
    print("❓ Ви точно впевнені що хочете видалити всі дані? Дані не можна буде повернути!")
    print("1. ✅ Так, я хочу видалити всі дані")
    print("2. ❌ Ні, я не хочу видаляти всі дані")
    while True:
        choice = input("Введіть ваш вибір: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                with open("HealthLog.txt", "w", encoding="utf-8") as file:
                    file.write("1\n")
                    file.write("\n")
                print("✅ Видалення даних проведено успішно!")
                print()
                break
            elif choice == 2:
                print("✅ Видалення даних успішно скасоване!")
                print()
                break
            else:
                print("❌ Ви не ввели конкретний пункт меню! Спробуйте ще раз.")
        else:
            print("❌ Ви не ввели цифру! Спробуйте ще раз.")




















