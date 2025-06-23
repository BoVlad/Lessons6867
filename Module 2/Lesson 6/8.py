for numb in range(1, 31):
    if numb % 3 == 0:
        print("Три")
        continue
    if numb % 5 == 0:
        print("П’ять")
        continue
    if numb % 15 == 0:
        print("ТриП’ять")
        continue
    else:
        print(numb)