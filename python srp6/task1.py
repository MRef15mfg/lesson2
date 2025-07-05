text = input("Введіть текст: ")

count = 0
for char in text:
    if char in ['.', '!', '?']:
        count += 1

print("Кількість речень у тексті:", count)
