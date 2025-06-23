textik = input("Напишіть текст для шифровки: ").lower()
for i in "аеєиіїоуюя":
        textik = textik.replace(i, "0")
for j in "бвгґджзйклмнпрстфхцчшщ":
        textik = textik.replace(j, "1")
print(textik)