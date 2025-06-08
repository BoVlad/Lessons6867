c = True
d = 1  #True
e = "Adolf"  #True
f = 0  #false
if c:
    print("True")
else:
    print("false")


# Методи форматування рядків:
#
# len(рядок) - повертає довжину рядка
# рядок.upper() - перетворює всі літери на великі
# рядок.lower() - перетворює всі літери на малі
# рядок.replace(стара_частина, нова_частина) - змінює "стару" частину в рядку на нову



text = "HEllo my brother the best"
print(len(text))
print(text.upper())
print(text.lower())
print(text.replace("brother", "hero"))



name2 = """це послідовності симв
олів, які використовуються для
зберігання тексту. Вони можуть мі
стити букви, цифри, пробіли та спеці
альні символи."""
print(name2)


print("12" * 10)


c = input("Input password > 8: ")
if len(c) < 8:
    print("Password short")
else:
    print("Password OK")

answer = "I love Pythoningingundjuice"

print(answer.replace("o", "@", 1))


if (answer.count("love")) > 0:
    print(answer.replace("love", "####"))

