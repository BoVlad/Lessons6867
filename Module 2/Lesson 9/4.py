from operator import truediv

dictionary = {"" : "Це нічого :)", }

while True:
    print("Введіть 1 для того що би подивитися чи є це слово в словнику")
    print("Введіть 2 для того що би ввести нову ключ-пару")
    print("Введіть 3 для того що би вийти")
    print()
    choice = input("Введіть ваш вибір: ")
    if choice.isdigit():
        if choice == 1:
            keychoice1 = input("Введіть ваше слово: ")
            if keychoice1 in dictionary:
                print("Так, це слово є!")
                print(dictionary[keychoice1])
                print()
            else:
                print("Такого слова немає :(")
                print()
        if choice == 2:
            keychoice2 = input("Введіть ваше слово: ")
            massagechoice2 = input("Введіть ваше слово: ")
            dictionary[keychoice2] = massagechoice2
            print("Ваша ключ пара успішно додана!")
            print()
        if choice == 3:
            break
        if choice != 1 or 2 or 3:
            print("Такої команди немає :(. Введіть іншу.")
            print()
    else:
        print("Це не цифра! Введіть іншу відповідь.")
        print()
