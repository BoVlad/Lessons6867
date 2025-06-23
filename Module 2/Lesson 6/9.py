cyrillic_to_latin = { 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h',
                      'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye',
                      'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i',
                      'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l',
                      'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
                      'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
                      'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
                      'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu',
                      'я': 'ia' }
text = input("Введіть текст для ''перекладення'': ")
for i in text:
    if i in cyrillic_to_latin:
        print(cyrillic_to_latin[i], end="")
    else:
        print(i, end="")
print()
print("Ось ваше ''перекладення'' :)")



