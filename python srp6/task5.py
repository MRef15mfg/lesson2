text = input("Введіть текст: ")
symbols = input("Введіть набір символів: ")

words = text.split()
result = ""

for word in words:
    has_bad_char = False
    for char in symbols:
        if char in word:
            has_bad_char = True
            break
    if not has_bad_char:
        result += word + " "

print("Результат:", result.strip())
