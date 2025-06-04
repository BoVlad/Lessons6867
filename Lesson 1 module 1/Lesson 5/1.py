ea = 123
print(f"lesson is god, but {ea} is better") # Принцип F-string

password = int(input("Введіть пароль: "))

while password != 1928:
    print(f"Пароль {password} не підходить, введіть інший.")
    password = int(input("Введіть пароль: "))
else:
    print(f"Пароль {password} підходить.")