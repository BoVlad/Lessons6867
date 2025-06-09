list = {"сонце": "sun",
        "кіт": "cat",
        "дерево": "tree",
        "книга": "book",
        "школа": "school",
        "друг": "friend",
        "їжа": "food",
        "музика": "music",
        "річка": "river",
        "мрія": "dream"}
word = input("Це перекладач. Введіть слово українською, яке ви хочете перекласти на англійську: ")
if word in list.keys():
    print(list.get(word))



