while True:
    print("Введіть температуру в Цельсія для конвертації")
    print("Введіть 0 для виходу")
    print()
    choice = input("Введіть ваш вибір: ")
    if choice.isdigit():
        choice = int(choice)
        if choice != 0:
            print("Введіть температуру для конвертації")
            print("1 - Кельвін")
            print("2 - Фаренгейт")
            print("Введіть 0 для виходу")
            print()
            choice2 = input("Введіть ваш вибір: ")
            if choice2.isdigit():
                choice2 = int(choice2)
                if choice2 == 0:
                    break
                elif choice2 == 1:
                    print(f"Ваші {choice} Цельсія в Кельвін буде становити {choice + 273.15} Кельвін!")
                    print()
                elif choice2 == 2:
                    print(f"Ваші {choice} Цельсія в Фаренгейт буде становити {choice * 1.8 + 32} Фаренгейт!")
                    print()
                else:
                    print("Ви не ввели потрібну позицію, спробуйте ще раз!")
                    print()
            else:
                print("Ви не ввели цифру, спробуйте ще раз!")
                print()
        if choice == 0:
            break
    else:
        print("Ви не ввели цифру, спробуйте ще раз!")
        print()