phone_book = {}

print("1. Додати контакт")
print("2. Пошук контакту")
print("3. Видалити контакт")

command = input("Введіть команду: ")

if command == "1":
    name = input("Введіть ім'я: ")
    number = input("Введіть номер телефону: ")
    phone_book[name] = number
    print("Контакт додано або оновлено.")
if command == "2":
    name = input("Введіть ім'я для пошуку: ")
    if name in phone_book:
        print("Номер телефону:", phone_book[name])
    else:
        print("Контакт не знайдено.")
if command == "3":
    name = input("Введіть ім'я для видалення: ")
    if name in phone_book:
        phone_book.pop(name)
        print("Контакт видалено.")
    else:
        print("Контакт не знайдено.")