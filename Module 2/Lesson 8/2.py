while True:
    answer = input("Введіть число: ")
    if answer.isdigit():
        sum = int(answer) + int(answer)
        print(sum)
    else:
        print("Це не цифра")
        continue


