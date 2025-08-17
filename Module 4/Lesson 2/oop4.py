class PersonMinecraft:
    def __init__(self, name, attack, speed):
        self.name = name
        self.attack = attack
        self.speed = speed

    def __str__(self):
        return f"I am cool {self.name}"

    def say_something(self):
        print(f"Це {self.name}, у нього непогана атака - {self.attack} хп, і швидкіть {self.speed} блок на секунду")


Steve = PersonMinecraft("Стів", 1, "1 - 3.5")
Steve.say_something()

Cow = PersonMinecraft("Корова", 0, "1 - 2")
Cow.say_something()

Skeleton = PersonMinecraft("Скелет", 4, 1)
Skeleton.say_something()

Sekret = PersonMinecraft("Одноступінчаста рідинна балістична ракета підводних човнів, яка у складі ракетного комплексу Д-4 перебувала на озброєнні підводних човнів", 20_000, 100)
Sekret.say_something()
