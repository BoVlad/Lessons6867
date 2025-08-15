numbers = [2, 5, 7, 67, 56, 23, 109, 1488, 6, 4]

def square(x):
    return x * x

new_fruits = list(map(square, numbers))
print(new_fruits)