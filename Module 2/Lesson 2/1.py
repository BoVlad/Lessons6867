# love кохати
# key value
# dict dictionary

my_dict = { "name": "Alice",
            "age": 10, "city":
            "Wonderland" }

print(my_dict["city"])  #Взяти значення але може викликати помилкуц якщо ключа немає
print(my_dict.get("country"))  #Взяти значення але не викликає помилку якщо ключа немає
a = my_dict.get("country", "Ukraine")  #Якщо значення не здайненене повертає по замовчуванню
if a is None:  #Перевірка на None
    print("Значення не знайдено")
else:
    print(a)


user = {}
user["name"] = "Andriy"
user["age"] = 13
print(user)

#del user["age"]  #Просто видаляє ключ
age = user.pop("age") #Видаляє ключ красивіше 🗿, з можливість записати видалене значення кудись
print(user)
print(age)

hobbies = { "Міккі Маус": "грати на гітарі",
            "Губка Боб": "ловити медуз",
            "Пікачу": "боротися зі злодіями",
            "Шрек": "жити в болоті",
            "Ельза": "керувати льодом" }
print(hobbies.get("Пікачу"))
# Завдання
print(hobbies.items())  # Виводить ключ і значення
print(hobbies.keys())  # Виводить ключ
print(hobbies.values())  # Виводить значення






