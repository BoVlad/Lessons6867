class Human:
    def __init__(self, title, hp, stamina, speed, level, attack):
        self.title = title
        self.hp = hp
        self.stamina = stamina
        self.speed = speed
        self.level = level
        self.attack = attack

    def __str__(self) -> str:
        return f"Race: {self.title}"


class Archer(Human):
    def __init__(self, level):
        self.title = "Archer"
        super().__init__(self.title, 80 + level*20, 95 + level*5, 3, level, 40 + level*5)


class Knight(Human):
    def __init__(self, level):
        self.title = "Knight"
        super().__init__(self.title, 80 + level*20, 105 + level*5, 5, level, 45 + level*5)


class Wizard(Human):
    def __init__(self, level):
        self.title = "Wizard"
        super().__init__(self.title, 80 + level*20, 95 + level*5, 3, level, 40 + level*5)


# from personages.race import Archer, Knight, Wizard
print("Welcome to game!")
name = input("Enter your name> ")
answer = 0
while answer not in [1, 2, 3]:
    answer = int(input("Choose role\n 1: Archer, 2: Knight, 3: Wizard> "))
    if answer == 1:
        hero = Archer(1)
    elif answer == 2:
        hero = Knight(1)
    elif answer == 3:
        hero = Wizard(1)
    else:
        print("Error! Try again")
        print(hero)


# _______

class Human:
    def __init__(self, title, hp, stamina, speed, level, attack, reload_time):
        self.title = title
        self.hp = hp
        self.stamina = stamina
        self.speed = speed
        self.level = level
        self.attack = attack
        self.reload_time = reload_time

    def __str__(self) -> str:
        return f"Race: {self.title}"


class Archer(Human):
    def __init__(self, level):
        self.title = "Archer"
        super().__init__(self.title, 80 + level*20, 95 + level*5, 3, level, 40 + level*5, 3)


class Knight(Human):
    def __init__(self, level):
        self.title = "Knight"
        super().__init__(self.title, 80 + level*20, 105 + level*5, 5, level, 45 + level*5, 2)


class Wizard(Human):
    def __init__(self, level):
        self.title = "Archer"
        super().__init__(self.title, 80 + level*20, 95 + level*5, 3, level, 40 + level*15, 5)


# _____________________

from datetime import datetime, timedelta


class Human:
    def __init__(self, title, hp, stamina, speed, level, attack, reload_time):
        self.title = title
        self.hp = hp
        self.stamina = stamina
        self.speed = speed
        self.level = level
        self.attack = attack
        self.reload_time = reload_time
        self.last_attack = None

    def __str__(self) -> str:
        return f"Race: {self.title}"

    def check_attack(self):
        if self.last_attack and datetime.now() - self.last_attack < timedelta(microseconds=self.reload_time):
            return False
        else:
            return True

    def attack_func(self):
        if self.check_attack():
            self.last_attack = datetime.now()
            print(f"Attacking {self.attack}")
            return self.attack
        else:
            print("Pls, wait!")
            return 0


class Archer(Human):
    def __init__(self, level):
        self.title = "Archer"
        super().__init__(self.title, 80 + level*20, 95 + level*5, 3, level, 40 + level*5, 300)


class Knight(Human):
    def __init__(self, level):
        self.title = "Knight"
        super().__init__(self.title, 80 + level*20, 105 + level*5, 5, level, 45 + level*5, 200)


class Wizard(Human):
    def __init__(self, level):
        self.title = "Archer"
        super().__init__(self.title, 80 + level*20, 95 + level*5, 3, level, 40 + level*15, 500)


# ________________

enemy1 = Knight(1)
print(f"Your enemy is {enemy1} \nHP is {enemy1.hp}")

enemy1.hp -= hero.attack_func()
enemy1.hp -= hero.attack_func()
enemy1.hp -= hero.attack_func()

print(f"Your enemy is {enemy1} HP is {enemy1.hp}")

enemy1 = Knight(1)
print(f"Your enemy is {enemy1} HP is {enemy1.hp}")

while enemy1.hp > 0 and hero.hp > 0:
    enemy1.hp -= hero.attack_func()
    if enemy1.hp > 0:
        hero.hp -= enemy1.attack_func()

if enemy1.hp <= 0:
    print("You win!")
else:
    print("You lose")

