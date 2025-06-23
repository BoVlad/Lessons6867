#break continium
count = 0
while True:
    number = int(input())
    if number == 0:
        break
    if number > 100:
        continue
    count = count + number
    print(count)
print(count)




