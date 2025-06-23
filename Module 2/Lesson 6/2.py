user = {}
user["name"] = "Andriy"
user["age"] = 15
user["name"] = "Kostya"
print(user)
print("⭐" * 50)

for key, value in user.items():
    print(f"{key} -> {value}")


