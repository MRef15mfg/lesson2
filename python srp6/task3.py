text = input("Введіть текст: ")

reserved = ["if", "else", "for", "while", "return", "def", "class"]
words = text.split()
result = ""

for word in words:
    if word in reserved:
        result += word.upper() + " "
    else:
        result += word + " "

print("Змінений текст:", result.strip())
