fruits = {"яблуко", "банан", "апельсин", "яблуко", "апельсин"}
print(fruits)
a = set("Kostyao")
b = set("182673817263719")
print(a)
print(b)

fruits.add("кавун")
fruits.add("драгонфрукт")
print(fruits)

fruits.remove("кавун")  # Видаляє, викликає помилку якщо елемента немає
fruits.discard("молоко")  # Видаляє, не викликає помилку якщо елемента немає
