phonebook = {}

while True:
    print("1. додати контакт")
    print("2. пошук контакту")
    print("3. видалити контакт")
    print("4. вийти")

    command = input("Введіть команду: ")

    if command == "1":
        name = input("Напишіть контакт, який хочете додати : ")
        phone = input("Напишіть номер, який хочете додати : ")
        print(f"Додається контакт {name} з номером {phone}")
        phonebook[name] = phone
    if command == "2":
        powyk = input("Напишіть контакт, який треба знайти: ")
        print(f"Знайдено контакт {powyk}")
    if command == "3":
        delete= input("Напишіть контакт, який треба видалити: ")
        print(f"{delete}")
    if command == "4":
        break

print(phonebook)