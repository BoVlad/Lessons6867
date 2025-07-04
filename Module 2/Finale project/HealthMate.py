import HealthMateDefs as HMD
import time

HMD.startmakefile()
# with open('HealthLog.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#
# for line in lines[1:6]:
#     print(line, end="")


while True:
    print(HMD.menu_visual)
    choice = input("Введіть ваш вибір: ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            HMD.choice1(time_now=time.time())
        elif choice == 2:
            HMD.choice2()
        elif choice == 3:
            HMD.choice3()
        elif choice == 4:
            HMD.choice4()
        elif choice == 5:
            break
        else:
            print("❌ Ви не ввели конкретний пункт меню! Спробуйте ще раз.")
            print()
    else:
        print("❌ Ви не ввели цифру! Спробуйте ще раз.")
        print()



