dishlist = []
import random
print("Привіт! Введіть вашу улюблену страву! Якщо ви хочете щоби ми зупинилися, то напишіть ''стоп''.")
while True:
    dialogue = random.randint(1, 3)
    dish = input("Почніть ввод: ")
    if dish != "стоп":
        dishlist.append(dish)
        if dialogue == 1:
            print(f"Круто, я також люблю {dish}! Давай пограємо ще!")
        if dialogue == 2:
            print(f"Не дуже люблю {dish}, але вона також непогана! Давай все одно пограємо ще!")
        if dialogue == 3:
            print(f"Я не люблю {dish}, але ми можемо пограти ще!")
    if dish == "стоп":
        break
print("Сумно, що ти виходиш. Бувай! Ти ввів такі страви:")
for key in dishlist:
    print(key)


