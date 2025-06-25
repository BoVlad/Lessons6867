import operations_p_generator
import string

print("------------------------------")
print("Це генератор пароля. ")
print("------------------------------")
print("Генератор цифрового пароля - 1")
print("Генератор літерного пароля - 2")
print("------------------------------")

menu = int(input("Введіть ваш вибір: "))

if menu == 1:
    len_of_p = int(input("Введіть довжину пароля: "))
    print("Ось ваш згенерований пароль: ", end="")
    operations_p_generator.p_number(len_of_p)
if menu == 2:


