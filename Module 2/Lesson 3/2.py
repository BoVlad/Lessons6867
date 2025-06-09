import random as r
print(r.random())
print(r.randint(10, 1000))
list = ["Andriy", "Vitaliy", "Ksenia", "Kolya", "Marina"]
print(r.shuffle(list))
print(list)
print(r.choice(list))


card = ["❤️", "♦️", "♣️", "♠️", "⭐"]
r.shuffle(card)
print(card)


card = ["❤️", "♦️", "♣️", "♠️", "⭐"]
card_random = ["❤️", "♦️", "♣️", "♠️", "⭐"]
r.shuffle(card_random)
sum = 0
while card_random != card:
    print(card_random)
    r.shuffle(card_random)
    sum = sum + 1
print(card_random)
print(sum)