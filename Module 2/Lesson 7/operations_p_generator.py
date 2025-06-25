import random
from random import randint

ascii_lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ascii_uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ascii_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def p_number(len_of_p):
    print("Ось ваш згенерований пароль: ", end="")
    for i in range(len_of_p):
        print(random.randint(0, 10), end="")
    return


def p_letter1(len_of_p):
    print("Ось ваш згенерований пароль: ", end="")
    for i in range(len_of_p):
        random.shuffle(ascii_lowercase)
        random.shuffle(ascii_lowercase)
        print(f"{ascii_lowercase[3]}", end="")
    return

def p_letter2(len_of_p):
    print("Ось ваш згенерований пароль: ", end="")
    for i in range(len_of_p):
        random.shuffle(ascii_uppercase)
        random.shuffle(ascii_uppercase)
        print(f"{ascii_uppercase[3]}", end="")
    return


def p_letter3(len_of_p):
    print("Ось ваш згенерований пароль: ", end="")
    for i in range(len_of_p):
        random.shuffle(ascii_letters)
        random.shuffle(ascii_letters)
        print(f"{ascii_letters[3]}", end="")
    return

    # whitespace = ' \t\n\r\v\f'
    # ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    # ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # ascii_letters = ascii_lowercase + ascii_uppercase
    # digits = '0123456789'
    # hexdigits = digits + 'abcdef' + 'ABCDEF'
    # octdigits = '01234567'
    # punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    # printable = digits + ascii_letters + punctuation + whitespace



