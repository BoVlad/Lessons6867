# minerals = “1011000011110001110001111000011111”
# Напишіть програму на Python, яка знаходить всі блоки золота та підраховує їх кількість. і вивести на єкран.
# золото = 1, камінь = 0

minerals = "1011000011110001110001111000011111"
gold = 0
stone = 0
for i in minerals:
    if i == "1":
        gold = gold + 1
    if i == "0":
        stone = stone + 1
print(f"Тут {gold} блоків золота і {stone} блоків каменю.")