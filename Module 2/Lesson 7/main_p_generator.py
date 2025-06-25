import operations_p_generator
import string

menu_list = """------------------------------
Це генератор пароля.
------------------------------
Генератор цифрового пароля - 1
Генератор літерного пароля - 2
Вийти - 3
------------------------------"""

while True:
    print()
    print()
    print(menu_list)
    print()
    menu = int(input("Введіть ваш вибір: "))
    if menu == 1:
        len_of_p = int(input("Введіть довжину пароля: "))
        operations_p_generator.p_number(len_of_p)
    if menu == 2:
        print()
        print("-----------------------------------------")
        print("Генератор літерного пароля маленькими - 1")
        print("Генератор літерного пароля великими - 2")
        print("Генератор літерного пароля впереміш - 3")
        print("-----------------------------------------")
        menu2 = int(input("Введіть ваш вибір: "))
        if menu2 == 1:
            len_of_p = int(input("Введіть довжину пароля: "))
            operations_p_generator.p_letter1(len_of_p)
        if menu2 == 2:
            len_of_p = int(input("Введіть довжину пароля: "))
            operations_p_generator.p_letter2(len_of_p)
        if menu2 == 3:
            len_of_p = int(input("Введіть довжину пароля: "))
            operations_p_generator.p_letter3(len_of_p)
    if menu == 3:
        break