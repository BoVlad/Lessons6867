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
        if choice == 2:
            HMD.choice2()
