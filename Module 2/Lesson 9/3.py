while True:
    try:
        answer1 = int(input("Input number 1 > "))
        answer2 = int(input("Input number 2 > "))
        c = answer1 / answer2
        print(c)
    except ValueError as error:
        print("It`s not number")
        print(error)
    except ZeroDivisionError as error:
        print("No zero division")
        print(error)
    else:
        print("No error")
    finally:
        print("Block finally")

