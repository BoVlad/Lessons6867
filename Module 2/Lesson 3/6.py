import random as r
numb_random = r.randint(1, 10)

print("Це гра-вгадайка. Вона генерує випадкове число від 1 до 10. Ви повинні вгадати це число.")
numb_player = int(input("Напишіть число: "))

while numb_player != numb_random:
    if numb_player > numb_random:
        print("Отакої! Ваше число завелике. Спробуйте число менше!")
    if numb_player < numb_random:
        print("Отакої! Ваше число замаленьке. Спробуйте число більше!")
    numb_player = int(input("Напишіть нове число: "))
else:
    print(f"Молодець! Ваше число {numb_player} співпало в загаданим числом {numb_random}!")














