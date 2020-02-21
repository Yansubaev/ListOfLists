inp = input().lower()
alphabet = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
rest = ""
for word in alphabet:
    for ch in inp:
        if ch == word:
            break
    else:
        rest += word
print(rest)
