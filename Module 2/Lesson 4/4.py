#fruits = ["apple", "banana", "pineapple", "cherry", "orange", "watermelon"]
#
#new_list = fruits[0:6:2]
#new_list = fruits[::-1]  #new_list.reverse
#print(new_list)

tasks = ["abobing", "kurkuming", "aizeyrbazhagning"]

print("-----")
menu = """My ToDo List
1. Додати
2. Видалити
3. Вивести список
-----"""

while True:
    print(menu)
    answer = int(input("Введіть номер задачі: "))
    if answer == 1:
        task = input("Введіть нове завдання: ")
        tasks.append(task)
        print("Завдання додано.")
        print("-----")
    if answer == 2:
        print("Список завдань:")
        numb_task = 1
        for task_pl in tasks:
            print(f"{numb_task}. {task_pl}")
            numb_task = numb_task + 1
        num = int(input("Введіть номер завдання для видалення: "))
        tasks.pop(num - 1)
        numb_task = 1
        for task_pl in tasks:
            print("Ось змінений список", end="")
            print(f"{numb_task}. {task_pl}")
            numb_task = numb_task + 1
        print("-----")
    if answer == 3:
        numb_task = 1
        for task_pl in tasks:
            print(f"{numb_task}. {task_pl}")
            numb_task = numb_task + 1
        print("-----")
